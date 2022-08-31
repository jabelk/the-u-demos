from netmiko import ConnectHandler
from getpass import getpass
import json
import csv

cisco1 = {
    "device_type": "cisco_ios_telnet",
    "host": "10.10.20.175",
    "username": "cisco",
    "password": "cisco",               # "password": getpass(),
}

command = "show ip interface brief"

# Will automatically 'disconnect()'
with ConnectHandler(**cisco1) as net_connect:
    print(net_connect.find_prompt())
    # show ip int brief raw text
    output = net_connect.send_command(command)
    print(output)
    # show ip int br fsm list of dicts parsed
    output_fsm = net_connect.send_command(command, use_textfsm=True)
    print(json.dumps(output_fsm, indent=4))

# https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file
csv_columns = ["intf", "ipaddr", "status", "proto"]
csv_file = "sh_ip_int_fsm.csv"
try:
    with open(csv_file, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_columns)
        writer.writeheader()
        for data in output_fsm:
            writer.writerow(data)
except IOError:
    print("I/O error")
