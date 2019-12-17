import configparser
import json


def cmd(func):
    conf = configparser.ConfigParser()
    conf.read("client.ini")
    host = conf.get("system", "host")
    port = conf.get("system", "port")
    with open("token.json", "r") as json_file:
        data = json.load(json_file)
    json_file.close()
    token = data["token"]
    headers = {"token": token}

    def wapper(*args, **kwargs):
        kwargs["url"] = "http://" + host + ":" + port + kwargs["url"]
        kwargs["headers"] = headers
        func(*args, **kwargs)
        return
    return wapper
