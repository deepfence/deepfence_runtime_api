import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def fetch_alerts(api_url, api_key, time_unit_number, time_unit):
    default_headers = {"Content-Type": "application/json", "Authorization": ""}
    api_response = requests.post("{0}/users/auth".format(api_url),
                                 json={"api_key": api_key}, headers=default_headers,
                                 verify=False).json()
    if api_response["success"]:
        print("Authentication successful")
    else:
        print("Authentication failed")
        return
    default_headers["Authorization"] = "Bearer " + api_response["data"]["access_token"]

    api_response = requests.post(
        "{0}/search?from=0&size=1000&&number={1}&time_unit={2}".format(api_url, time_unit_number, time_unit),
        json={"_type": "alert", "_source": [], "filters": {"masked": ["false"], "type": ["alert"]}, "node_filters": {}},
        headers=default_headers, verify=False).json()

    alerts = api_response.get("data", {}).get("hits", [])

    return alerts


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 5:
        print("Usage: python3 fetch_alerts.py <mgmt_console_ip_address> <api_key> <time_unit_number> <time_unit>")
        # i.e. python3 user_activity.py 167.71.71.71 042c1cd3-0fcc-40e5-8f74-6e6c1d3eca92 1 minute
        # time_unit: minute | hour | day | month
        exit(1)
    alerts = fetch_alerts("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4])
    print(alerts)
