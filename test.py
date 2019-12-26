import requests
import json


if __name__ == '__main__':
    headers = {"token": "aByAGqFDd7"}
    body = {"password": "stp@2019"}
    body = json.dumps(body)
    result = requests.post(url="http://39.97.124.216:9188/system/v1/process",
                           headers=headers,
                           data=body)
    print(result.json())
