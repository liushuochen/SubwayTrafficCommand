# /etc/bashrc
import sys

if __name__ == '__main__':
    arg_list = sys.argv
    if arg_list[1] == "version":
        import version
        version.get_version(url="/system/v1/version")

    elif arg_list[1] == "system":
        try:
            if arg_list[2] == "start":
                import system
                system.start(url="/system/v1/login")
                print("SubwayTraffic service running")
            elif arg_list[2] == "status":
                import service_status
                service_status.show_status(url="/system/v1/live")
            elif arg_list[2] == "stop":
                import stop
                stop.stop(url="/system/v1/process")
            else:
                print("bash: command not found")
        except IndexError:
            print("bash: command not found")

    elif arg_list[1] == "stop":
        import stop
        stop.stop(url="/system/v1/process")
    elif arg_list[1] == "user":
        try:
            if arg_list[2] == "list":
                import user
                user.user_list(url="/user/v1/users")
            else:
                print("bash: command not found")
        except IndexError:
            print("bash: command not found")

    else:
        print("bash: command not found")
