#!/usr/bin/python3
from netmiko import ConnectHandler
from argparse import ArgumentParser
import sys
# https://mkaz.blog/code/python-argparse-cookbook/


# single device input
# next demo feed in device list from csv

# arg parser configuration
parser = ArgumentParser(prog="Netmiko command line tool", description="Netmiko command line tool",
                        usage="python3 3-netmiko-argparse.py -u USER -p PASS -d IP_ADDR -c \"show int ip brief\"")
parser.add_argument("-u", "--user", help="Username of device.",
                    type=str, dest="user", required=True)
parser.add_argument("-p", "--pass", help="password",
                    type=str, dest="password", required=True)
parser.add_argument("-d", "--device", help="IP address of cisco asa",
                    type=str, dest="device", required=True)
parser.add_argument("-c", "--cmd", help="cisco asa command",
                    type=str, dest="cmd", required=True)
parser.add_argument(
    "--port", help="ssh port if not define it is 22 by default.", type=int, dest="port")

# if no argument is supplied print help message.
if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

# netmiko configuration
asa_config = dict(
    username=args.user,
    password=args.password,
    ip=args.device,
    device_type="cisco_asa",
    port=args.port if args.port else 22
)

with ConnectHandler(**asa_config) as asa:
    result = asa.send_command(args.cmd)

# print out the result
print(result)


# if __name__ == "__main__":

#     facts = {'vendor': 'cisco', 'mgmt_ip': '10.1.1.1',
#              'model': 'nexus', 'hostname': 'NYC301', 'os': '6.1.2'}

#     parser = argparse.ArgumentParser(
#         description='Python Argparse Demo for Training Course.')
#     parser.add_argument('-f', '--fact', choices=facts.keys(),
#                         help='enter a valid fact from the device facts dictionary')
#     parser.add_argument(
#         '-u', '--user', help='enter username to login to the device')
#     parser.add_argument('-p', '--password', required=True,
#                         help='enter password to login to the device')
#     parser.add_argument('-d', '--device_type',
#                         help='enter device type for netmiko')
#     parser.add_argument(
#         '-i', '--ipaddr', choices=['csr1', 'csr2'], help='enter ipaddress for netmiko')
#     parser.add_argument(
#         '-c', '--cmd', choices=['show version', 'show run'], help='enter command to execute for netmiko')
#     args = parser.parse_args()
