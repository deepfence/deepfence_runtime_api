from datetime import datetime, timedelta

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from collections import defaultdict

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def split_list_into_chunks(my_list: list, size: int) -> list:
    def divide_chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    return list(divide_chunks(my_list, size))


def delete_alerts(api_url, api_key, days_ago):
    days_ago = int(days_ago)
    if days_ago < 1:
        print("days_ago should be greater than 0")
        return

    # Auth
    default_headers = {"Content-Type": "application/json"}
    auth_response = requests.post("{0}/users/auth".format(api_url), json={"api_key": api_key}, headers=default_headers,
                                  verify=False).json()
    if auth_response["success"]:
        print("Authentication successful")
    else:
        print("Authentication failed")
        return
    default_headers["Authorization"] = "Bearer " + auth_response["data"]["access_token"]

    today = datetime.utcnow()
    n_days_ago = today - timedelta(days=int(days_ago))
    print("Deleting alerts before "+n_days_ago.strftime("%H:%M:%S, %d %B %Y"))

    es_from = 0
    page_size = 5000
    alert_ids_to_delete = []
    while True:
        if es_from + page_size >= 50000:
            break
        alerts_summary = requests.post(
            "{0}/search?from={1}&size={2}&lucene_query=&number=365&time_unit=day".format(api_url, es_from, page_size),
            json={"_type": "alert", "_source": ["_id", "@timestamp"],
                  "filters": {"masked": ["false", "true"]}},
            headers=default_headers, verify=False).json()
        if not alerts_summary.get("success", False):
            print(alerts_summary.get("error", ""))
            return
        if not alerts_summary["data"]["hits"]:
            break

        for alert in alerts_summary["data"]["hits"]:
            alert_date = datetime.strptime(alert["_source"]["@timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
            if alert_date < n_days_ago:
                alert_ids_to_delete.append(alert["_id"])
        es_from += page_size

    if not alert_ids_to_delete:
        print("No alerts to delete")
        return

    print("Total alerts to delete: "+str(len(alert_ids_to_delete)))
    for alert_ids in split_list_into_chunks(alert_ids_to_delete, 500):
        print(requests.post("{0}/docs/delete_by_id".format(api_url),
                            json={"ids": alert_ids, "index_name": "alert", "doc_type": "alert"},
                            headers=default_headers, verify=False).text)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 delete_alerts_by_time.py <mgmt_console_ip_address> <api_key> <delete_before_number_of_days>")
        exit(1)
    delete_alerts("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2], sys.argv[3])
