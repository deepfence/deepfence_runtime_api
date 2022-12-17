import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from collections import defaultdict

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def split_list_into_chunks(my_list: list, size: int) -> list:
    def divide_chunks(l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    return list(divide_chunks(my_list, size))


def get_blocked_ips(api_url, api_key):
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
    page_no = 1
    page_size = 500
    alerts_summary = requests.post(
        "{0}/search?from=0&size=10000&lucene_query=&number=365&time_unit=day".format(api_url, page_no, page_size),
        json={"_type": "alert", "_source": ["_id", "classtype", "masked"], "filters": {"masked": ["false", "true"]}},
        headers=default_headers, verify=False).json()
    if not alerts_summary.get("success", False):
        print(alerts_summary.get("error", ""))
        return
    classtypes = defaultdict(int)
    masked_classtypes = defaultdict(int)
    for hit in alerts_summary["data"]["hits"]:
        if hit["_source"]["masked"] == "true":
            masked_classtypes[hit["_source"]["classtype"]] += 1
        else:
            classtypes[hit["_source"]["classtype"]] += 1
    if not classtypes and not masked_classtypes:
        print("No alerts found")
        return

    classtypes = [{"classtype": k, "count": v} for k, v in classtypes.items()]
    masked_classtypes = [{"classtype": k, "count": v} for k, v in masked_classtypes.items()]
    print("\nAlert classtype with count")
    for i, classtype in enumerate(classtypes):
        print("{0}. {1}\t{2}".format(i + 1, classtype["classtype"], classtype["count"]))
    classtypes_len = len(classtypes)
    print("\nAlert classtype with count (Masked alerts)")
    for i, classtype in enumerate(masked_classtypes):
        print("{0}. {1}\t{2}".format(classtypes_len + i + 1, classtype["classtype"], classtype["count"]))

    print("\nEnter comma separated list of classtypes to delete. Eg: 1,3,4")
    user_input = input("-->").split(",")
    selected_classtypes = []
    selected_masked_classtypes = []
    for user_input_no in user_input:
        try:
            if int(user_input_no) > classtypes_len:
                class_type = masked_classtypes[int(user_input_no) - classtypes_len - 1]["classtype"]
                selected_masked_classtypes.append(class_type)
                print("Deleting \"{0}\" alerts (masked)".format(class_type))
            else:
                class_type = classtypes[int(user_input_no) - 1]["classtype"]
                selected_classtypes.append(class_type)
                print("Deleting \"{0}\" alerts".format(class_type))
        except Exception as ex:
            print(ex)

    alert_id = []
    for classtype in selected_classtypes:
        for hit in alerts_summary["data"]["hits"]:
            if hit["_source"]["masked"] != "true" and hit["_source"]["classtype"] == classtype:
                alert_id.append(hit["_id"])
    for classtype in selected_masked_classtypes:
        for hit in alerts_summary["data"]["hits"]:
            if hit["_source"]["masked"] == "true" and hit["_source"]["classtype"] == classtype:
                alert_id.append(hit["_id"])
    for alert_ids in split_list_into_chunks(alert_id, 500):
        print(requests.post("{0}/docs/delete_by_id".format(api_url),
                            json={"ids": alert_ids, "index_name": "alert", "doc_type": "alert"},
                            headers=default_headers, verify=False).text)


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 delete_alerts.py <mgmt_console_ip_address> <api_key>")
        exit(1)
    get_blocked_ips("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2])
