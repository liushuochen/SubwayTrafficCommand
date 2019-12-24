import os
import util
import requests
import json
import configparser
import time


@util.cmd
def start(**kwargs):
    os.system("cd /opt/SubwayTraffic\nnohup python main.py >nohup 2>&1 &")
    conf = configparser.ConfigParser()
    conf.read("/opt/SubwayTrafficCommand/client.ini")
    body = {
        "email": conf.get("admin", "email"),
        "password": conf.get("admin", "pwd")
    }
    body = json.dumps(body)
    time.sleep(3)
    result = requests.post(data=body, **kwargs)
    message = result.json()
    code = message["code"]
    if code == 200:
        token = message["token"]
        data = {"token": token}
        data = json.dumps(data, indent=4)
        with open("/opt/SubwayTrafficCommand/token.json", "w") as json_file:
            json_file.write(data)
        json_file.close()
    else:
        print("login admin user error:", message)
