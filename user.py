import util
import requests
import prettytable


@util.cmd
def user_list(**kwargs):
    result = requests.get(**kwargs)
    message = result.json()
    if result.status_code == 200:
        users = message["users"]
        table = prettytable.PrettyTable()
        table.field_names = ["uuid", "email", "status"]
        for user in users:
            table.add_row([user["uuid"], user["email"], user["status"]])
        print(table)
    else:
        print("error:", message["error"])
