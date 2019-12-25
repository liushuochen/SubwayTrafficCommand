import prettytable
import requests
import util


@util.cmd
def show_status(**kwargs):
    status = "unknown"
    try:
        result = requests.get(**kwargs)
        message = result.json()
        if message["code"] == 200:
            status = "active"
    except Exception:
        status = "fault"

    table = prettytable.PrettyTable()
    table.field_names = ["service name", "status"]
    table.add_row(["SubwayTraffic", status])
    print(table)


if __name__ == '__main__':
    show_status(url="/system/v1/live")