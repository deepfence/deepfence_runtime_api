package main

import (
	"crypto/tls"
	"flag"
	"fmt"
	"github.com/gorilla/websocket"
	"log"
	"net/http"
	"os"
	"time"
)

var nodeType = flag.String("node_type", "host", fmt.Sprintf("Node type to run websocket client for. Ex: host, container, container_image, container_by_name, process, process_by_name, pod, kube_service, kube_controller"))
var apiUrl = flag.String("api_url", "", "Enter api url. Ex: 22.33.44.55")
var apiKey = flag.String("api_key", "", "Enter api key. (Get it from user management page)")
var stopped = flag.String("stopped", "running", "Filter by stopped status: stopped | running | both")
var pseudo = flag.String("pseudo", "hide", "Filter by pseudo status: show | hide")
var unconnected = flag.String("unconnected", "hide", "Filter by unconnected status: show | hide")
var namespace = flag.String("namespace", "", "Filter by namespace (for kubernetes)")

func connectWS() *websocket.Conn {
	wsUrl := fmt.Sprintf("wss://%s/ws?node_type=%s&stopped=%s&pseudo=%s&unconnected=%s&namespace=%s&api_key=%s", *apiUrl, *nodeType, *stopped, *pseudo, *unconnected, *namespace, *apiKey)
	fmt.Printf("Connecting to %s", wsUrl)
	dialer := &websocket.Dialer{
		Proxy:            http.ProxyFromEnvironment,
		HandshakeTimeout: 45 * time.Second,
		TLSClientConfig:  &tls.Config{InsecureSkipVerify: true},
	}
	conn, _, err := dialer.Dial(wsUrl, nil)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	return conn
}

func main() {
	flag.Parse()
	log.SetFlags(0)
	ws := connectWS()
	for {
		_, resp, err := ws.ReadMessage()
		if err != nil {
			fmt.Println("read:", err)
			return
		}
		fmt.Println("\nGot data:\n", string(resp))
	}
}
