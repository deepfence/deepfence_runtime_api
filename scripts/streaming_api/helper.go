package main

import (
	"crypto/tls"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
	"time"
)

type authJSON struct {
	Data struct {
		AccessToken  string `json:"access_token"`
		RefreshToken string `json:"refresh_token"`
	} `json:"data"`
	Error   interface{} `json:"error"`
	Success bool        `json:"success"`
}

func getAccessToken(apiUrl string, apiKey string) string {
	var authJson authJSON
	url := fmt.Sprintf("https://%s/deepfence/v1.5/users/auth", apiUrl)
	method := "POST"

	payload := strings.NewReader(fmt.Sprintf(`{"api_key" : "%s"}`, apiKey))

	tr := &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}
	client := &http.Client{Transport: tr}
	req, err := http.NewRequest(method, url, payload)

	if err != nil {
		fmt.Println(err)
		return ""
	}
	req.Header.Add("Content-Type", "application/json")

	res, err := client.Do(req)
	if err != nil {
		fmt.Println(err)
		return ""
	}
	defer res.Body.Close()

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		fmt.Println(err)
		return ""
	}

	json.Unmarshal(body, &authJson)
	return authJson.Data.AccessToken
}

func startVulnerabilityScan(nodeId string, accessToken string, nodeType string, apiUrl string) error {
	url := fmt.Sprintf("https://%s/deepfence/v1.5/node/0/cve_scan_start?scope_id=%s&node_type=%s&priority=false", apiUrl, nodeId, nodeType)
	payload := strings.NewReader(`{"user_defined_tags":[],"scan_type":["base","java","python","ruby","php","javascript","rust","golang","dotnet"],"scan_this_cluster":false,"scan_this_namespace":false}`)

	// wait till node is ready for scan
	time.Sleep(30 * time.Second)

	client := &http.Client{Transport: &http.Transport{
		TLSClientConfig: &tls.Config{InsecureSkipVerify: true},
	}}
	req, err := http.NewRequest("POST", url, payload)
	if err != nil {
		return err
	}
	req.Header.Add("Content-Type", "application/json")
	req.Header.Add("Authorization", fmt.Sprintf("Bearer %s", accessToken))

	res, err := client.Do(req)
	if err != nil {
		return err
	}
	defer res.Body.Close()

	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		return err
	}
	fmt.Println(nodeId + ": " + string(body))
	return nil
}
