package main

import (
	"crypto/tls"
	"encoding/json"
	"flag"
	"fmt"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/gorilla/websocket"
)

var nodeID = flag.String("node_type", "hosts", "Node type to run websocket client for. Ex: hosts, containers, containers-by-image, kubernetes-clusters, cloud-providers, cloud-regions, processes")
var apiUrl = flag.String("api_url", "", "Enter api url. Example: 22.33.44.55 / abc.com")
var apiKey = flag.String("api_key", "", "Enter api key. (Get it from user management page)")
var ignoreConnections = flag.Bool("ignore_connections", true, "Weather to ignore connections data")
var vulnerabilityScan = flag.Bool("vulnerability_scan", true, "Start vulnerability scan on new nodes")

func connectWS() (*websocket.Conn, error) {
	wsUrl := fmt.Sprintf("wss://%s/topology-api/topology-connection-ws?t=5s&ignore_connections=%s&api_key=%s",
		*apiUrl, strconv.FormatBool(*ignoreConnections), *apiKey)
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
		accessToken = getAccessToken(*apiUrl, *apiKey)
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
				return
			}
			for _, nodeInfo := range topologyDiff.Nodes.Add {
				fmt.Printf("found new node %#v, starting scan for  \n", nodeInfo.ID)
				if *nodeID == "hosts" {
					nodeType = "host"
				} else if *nodeID == "containers" {
					nodeType = "container"
				} else if *nodeID == "containers-by-image" {
					nodeType = "container_image"
				} else {
					fmt.Println("vulnerability scan not applicable for node: " + nodeInfo.Label)
					continue
				}
				nodeInfo := nodeInfo
				go func() {
					err := startVulnerabilityScan(nodeInfo.ID, accessToken, nodeType, *apiUrl)
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
