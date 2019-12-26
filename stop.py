import util
import configparser
import json
import requests
import os


@util.cmd
def stop(**kwargs):
    conf = configparser.ConfigParser()
    conf.read("/opt/SubwayTrafficCommand/client.ini")
    body = {
        "email": conf.get("admin", "email"),
        "password": conf.get("admin", "pwd")
    }
    body = json.dumps(body)
    result = requests.post(data=body, **kwargs)
    message = result.json()
    http_code = result.status_code
    if http_code == 200:
        pro_list = message["process"].sort(reverse=True)
    else:
        print("stop service error:", message)
        return

    for pro in pro_list:
        os.kill(pro, 9)
    print("stop SubwayTraffic service success")
