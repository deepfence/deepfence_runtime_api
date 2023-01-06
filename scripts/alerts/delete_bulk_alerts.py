import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from collections import defaultdict

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def delete_threshold_alerts(api_url, api_key):
    default_headers = {"Content-Type": "application/json"}
    auth_response = requests.post("{0}/users/auth".format(api_url), json={"api_key": api_key}, headers=default_headers,
                                      verify=False).json()
    if auth_response["success"]:
       print("Authentication successful")
    else:
       print("Authentication failed")
       return
    default_headers["Authorization"] = "Bearer " + auth_response["data"]["access_token"]
    es_from = 0
    page_size = 5000
    alerts = []
    classtypes = defaultdict(int)
    masked_classtypes = defaultdict(int)
    while True:
        alerts_summary = requests.post(
            "{0}/search?from={1}&size={2}&lucene_query=&number=1&time_unit=hour".format(api_url, es_from, page_size),
            json={"_type": "alert", "_source": ["_id", "classtype", "masked", "summary", "count"],
                  "filters": {"masked": "false"}},
            headers=default_headers, verify=False).json()
        if not alerts_summary.get("success", False):
            print(alerts_summary.get("error", ""))
            return
        if not alerts_summary["data"]["hits"]:
            break
        alerts.extend(alerts_summary["data"]["hits"])
        es_from += page_size
        counter = 1
    for alert in alerts:
        if alert["_source"]["count"]>10000:
            payload = json.dumps({
            "docs" : {
                "_id": alert["_id"],
                "_index": "alert",
                "_type": "alert",
                "summary": alert["_source"]["summary"],
                "classtype": alert["_source"]["classtype"],
            }})
            counter += 1
            try:
                res = requests.post("{0}/maskedalerts".format(api_url), data=payload,
                headers=default_headers, verify=False)
                if res.status_code != 200:
                    raise Exception(res.text)
            except Exception as e:
                print(e)
                continue


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 delete_bulk_alerts.py <mgmt_console_ip_address> <api_key>")
        exit(1)
    delete_threshold_alerts("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2])
