import sys

if __name__ == '__main__':
    arg_list = sys.argv
    if arg_list[1] == "version":
        import version
        version.get_version(url="/system/v1/version")
    elif arg_list[1] == "start":
        import start
        start.start(url="/system/v1/login")
        print("SubwayTraffic service running")
    else:
        print("bash: command not found")
