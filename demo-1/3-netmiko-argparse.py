#!/usr/bin/python3
from netmiko import ConnectHandler
from argparse import ArgumentParser
from getpass import getpass

if __name__ == "__main__":

    parser = ArgumentParser(
        description="Netmiko command line tool",
        usage="python3 3-netmiko-argparse.py -u cisco -d cisco_ios_telnet  -i 10.10.20.175 -c 'show ip interface brief' -f command_output.txt",
    )
    parser.add_argument(
        "-u",
        "--user",
        help="Supply a username to login to the device",
    )
    parser.add_argument(
        "-p",
        "--password",
        help="Supply a password to login to the device, if none is given, you will be prompted for one",
    )
    parser.add_argument(
        "-d",
        "--device_type",
        choices=[
            "cisco_ios_telnet",
            "cisco_xr_telnet",
            "cisco_ios",
            "cisco_nxos",
            "cisco_asa",
            "cisco_xr",
        ],
        help="Choose a device type for the Netmiko connection",
        required=True,
    )
    parser.add_argument(
        "-i",
        "--ipaddr",
        choices=["10.10.20.175", "10.10.20.176"],
        help="Supply an IP address for Netmiko, choices from the Sandbox",
        required=True,
    )
    parser.add_argument(
        "-c",
        "--cmd",
        choices=[
            "show version",
            "show run",
            "show ip interface brief",
        ],
        help="Supply a command to execute to the device from the choices",
        required=True,
    )
    parser.add_argument(
        "-f",
        "--file",
        help="If you want to save the output to a file, enter the filename here",
    )
    args = parser.parse_args()

    if not args.password:
        args.password = getpass()

    device_dict = {
        "device_type": args.device_type,
        "host": args.ipaddr,
        "username": args.user,
        "password": args.password,
    }

    netmiko_device = ConnectHandler(**device_dict)
    command_output = netmiko_device.send_command(args.cmd)
    print(command_output)

    if args.file:
        with open(args.file, "w") as file:
            file.write(command_output)
