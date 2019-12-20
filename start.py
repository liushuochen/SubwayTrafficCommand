import os


def start():
    os.system("cd /opt/SubwayTraffic\nnohup python main.py >nohup 2>&1 &")
