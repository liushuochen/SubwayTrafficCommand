import requests
import util


@util.cmd
def get_version(**kwargs):
    result = requests.get(**kwargs)
    message = result.json()
    code = message["code"]
    if code == 200:
        print(message["version"])
    else:
        print("get version error:", message["error"])
