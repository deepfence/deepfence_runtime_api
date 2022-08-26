package main

import (
	"crypto/tls"
	"encoding/json"
	"flag"
	"fmt"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/gorilla/websocket"
)

var nodeIDs = []string{"hosts", "containers", "containers-by-image", "kubernetes-clusters", "cloud-providers", "cloud-regions", "processes"}
var nodeID = flag.String("node-type", "hosts", fmt.Sprintf("Node type to run websocket client for. Ex: %s", strings.Join(nodeIDs, ", ")))
var managementConsoleUrl = flag.String("management-console-url", "", "Enter api url. Example: 22.33.44.55 / abc.com")
var deepfenceKey = flag.String("deepfence-key", "", "Enter api key. (Get it from user management page)")
var ignoreConnections = flag.Bool("ignore-connections", true, "Weather to ignore connections data")
var vulnerabilityScan = flag.Bool("vulnerability-scan", false, "Start vulnerability scan on new nodes")

func connectWS() (*websocket.Conn, error) {
	wsUrl := fmt.Sprintf("wss://%s/topology-api/topology-connection-ws?t=5s&ignore_connections=%s&api_key=%s",
		*managementConsoleUrl, strconv.FormatBool(*ignoreConnections), *deepfenceKey)
	fmt.Printf("Connecting to %s\n", wsUrl)
	dialer := &websocket.Dialer{
		Proxy:            http.ProxyFromEnvironment,
		HandshakeTimeout: 45 * time.Second,
		TLSClientConfig:  &tls.Config{InsecureSkipVerify: true},
	}
	conn, _, err := dialer.Dial(wsUrl, nil)
	if err != nil {
		return nil, err
	}
	return conn, nil
}

func main() {
	var topologyDiff TopologyDiff
	var accessToken string
	var nodeType string
	flag.Parse()
	if *managementConsoleUrl == "" {
		fmt.Println("management-console-url is required")
		os.Exit(1)
	} else if *deepfenceKey == "" {
		fmt.Println("deepfence-key is required")
		os.Exit(1)
	}
	if !inSlice(nodeIDs, *nodeID) {
		fmt.Printf("node-type must be one of %s", strings.Join(nodeIDs, ", "))
		os.Exit(1)
	}
	ws, err := connectWS()
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	sendMessage := func(msg string) error {
		msgJson := map[string]interface{}{}
		err := json.Unmarshal([]byte(msg), &msgJson)
		if err != nil {
			return err
		}
		err = ws.WriteJSON(msgJson)
		if err != nil {
			return err
		}
		return nil
	}

	go func() {
		err := sendMessage(fmt.Sprintf(`{"add":{"topology_id":"","node_id":"","children":[{"topology_id":"%s"}]}}`, *nodeID))
		if err != nil {
			fmt.Println(err)
			os.Exit(1)
		}
	}()

	if *vulnerabilityScan {
		accessToken = getAccessToken(*managementConsoleUrl, *deepfenceKey)
	}

	for {
		_, resp, err := ws.ReadMessage()
		if err != nil {
			fmt.Println(err)
			return
		}
		if *vulnerabilityScan {
			err := json.Unmarshal(resp, &topologyDiff)
			if err != nil {
				fmt.Println(err)
				return
			}
			for _, nodeInfo := range topologyDiff.Nodes.Add {
				fmt.Printf("Starting vulnerability scan on new node %s\n", nodeInfo.Label)
				if *nodeID == "hosts" {
					nodeType = "host"
				} else if *nodeID == "containers" {
					nodeType = "container"
				} else if *nodeID == "containers-by-image" {
					nodeType = "container_image"
				} else {
					fmt.Printf("vulnerability scan not applicable for node: %s\n", nodeInfo.Label)
					continue
				}
				nodeInfo := nodeInfo
				go func() {
					err := startVulnerabilityScan(nodeInfo.ID, accessToken, nodeType, *managementConsoleUrl)
					if err != nil {
						fmt.Println(err)
					}
				}()
			}
		} else {
			fmt.Println("\nGot data:\n", string(resp))
		}
	}
}

func inSlice(slice []string, val string) bool {
	for _, item := range slice {
		if item == val {
			return true
		}
	}
	return false
}
