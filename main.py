import sys

if __name__ == '__main__':
    arg_list = sys.argv
    if arg_list[1] == "version":
        import version
        version.get_version(url="/system/v1/version")
