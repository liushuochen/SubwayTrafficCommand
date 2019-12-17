import os


def start():
    os.system("nohup python /opt/SubwayTraffic/main.py >nohup 2>&1 &")
