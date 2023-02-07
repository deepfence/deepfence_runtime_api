from urllib import response
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from datetime import datetime
from dateutil import tz,parser

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def user_activity_log(api_url, api_key,from_time,to_time):
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

    # "2023-01-31T00:00:00+05:30", 
    # "2023-02-06T00:00:00+05:30"},
    api_response = requests.post("{0}/user-activity-log".format(api_url),
                                 json={"from_time" : from_time ,"to_time" : to_time},
                                 headers=default_headers, verify=False).json()
    
    audit_logs = api_response.get("data", {}).get("user_audit_logs", [])
    if audit_logs:
        for log in audit_logs:
            parsed_created_at = parser.parse(log["created_at"]).astimezone(tz.tzlocal())
            log["created_at"] = str(parsed_created_at)
    
    return audit_logs


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 5:
        print("Usage: python3 user_activity.py <mgmt_console_ip_address> <api_key> <timestring_iso_format:from_time> <timestring_iso_format:to_time>")
        # i.e. python3 user_activity.py 167.71.236.9 042c1cd3-0fcc-40e5-8f74-6e6c1d3eca92 "2023-01-31T00:00:00+05:30" "2023-02-06T00:00:00+05:30"
        exit(1)
    user_audit_logs = user_activity_log("https://{0}/deepfence/v1.5".format(sys.argv[1]), sys.argv[2],sys.argv[3],sys.argv[4])
    print(user_audit_logs)
