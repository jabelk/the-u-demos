#!/usr/bin/python3
from netmiko import ConnectHandler
from getpass import getpass

if __name__ == "__main__":
    device_dict = {
        "device_type": "cisco_ios_telnet",
        "host": "10.10.20.175",
        "username": "cisco",
        "password": getpass(),
    }

    netmiko_device = ConnectHandler(**device_dict)
    print(netmiko_device.find_prompt())
    print(
        netmiko_device.send_command(
            "show version | include Version"
        )
    )
    netmiko_device.disconnect()
