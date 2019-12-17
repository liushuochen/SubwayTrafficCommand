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
        print("error")


if __name__ == '__main__':
    get_version(url="/system/v1/version")
