# Demo 1: Building your first Netmiko scripts

Goal: Use Netmiko read-only show commands to get operational data and build a CLI tool to scale it to share with others.

These examples were built using the [NSO Reservable Sandbox](https://devnetsandbox.cisco.com/RM/Diagram/Index/43964e62-a13c-4929-bde7-a2f68ad6b27c?diagramType=Topology), not because we are using NSO, it just has a nice topology to use. The network devices have telnet connections exposed in this sandbox, so I used the telnet Netmiko connections. The scripts were run in a local virtual environment with VPN access to the Sandbox. Check out the `requirements.txt` file for which version of Netmiko that was used, though most versions should work.

> Note: These examples use Netmiko 4.0.0 because 4.1.0 and greater require Python 3.7 minimum and my local Python was 3.6. You can use newer version of Netmiko if you have Python 3.7+ installed.

## First Script: 1-netmiko-intro.py

[Netmiko](https://ktbyers.github.io/netmiko/#api-documentation) is a Python "Multi-vendor library to simplify Paramiko SSH connections to network devices." Paramiko is a popular general purpose SSH connection Python library, but requires a bit of extra coding to handle a lot of the details when connecting to network devices. Rather than reinventing the wheel, many network automation engineers use Netmiko because it is free and open-source, with support for common network CLI platforms such as Cisco IOS, Nexus, IOS-XR and other vendors platforms as well.

Netmiko uses an [factory function design](https://realpython.com/factory-method-python/) to select the proper  [Python Class](https://ktbyers.github.io/netmiko/docs/netmiko/index.html#netmiko.ConnectHandler) out of the possible platforms supported. The typical usage for the `ConnectHandler` class is to either provide inputs for the parameters needed (device type, hostname / IP address, username and password), or providing a dictionary with the properly named keys, along with the `**` which tells Python to unpack the dictionary and plug it into the parameters.

```python
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
    print(dir(netmiko_device))
    netmiko_device.disconnect()
```

This very small script has a couple of things to note:

- `if __name__ == "__main__":` is used so that if the script was imported the code will not run, but if it is run as a standalone script, it will run the right lines. You will see this for the other scripts as well.
- I used `getpass()` to get the password from the user as a prompt. This is a security best-practice if you are not using a password manager like Hashicorp Vault because you do not want to have passwords stored in plaintext in your code. `getpass()` does the heavy lifting for us because it also hides the input while you are typing it in.
- We create a Python object called `netmiko_device`, which has methods that apply to all device types like `send_command` and ones specific to the IOS device type. I print out the listed methods using `dir()` on the `netmiko_device` so you can see all the possible options.

## Second Script: 2-netmiko-show.py

In this script I am using Netmiko to send a "show ip interface brief" command to a Cisco IOS device, and then leverage the TextFSM parsing feature of Netmiko to turn the operational data string into a structured data object. Once the data is in a structured data object, in this case a list of dictionaries that looks like this:

```python
[
    {
        "intf": "GigabitEthernet1",
        "ipaddr": "10.10.20.175",
        "status": "up",
        "proto": "up"
    },
    {
        "intf": "GigabitEthernet2",
        "ipaddr": "172.16.252.21",
        "status": "up",
        "proto": "up"
    },
....

```

I then feed that nested data structure into a CSV file, using the dictionary keys for each list entry as the column headers. The resulting report is a CSV file that can then be shared with other engineers or stakeholders. This same process could be scaled to multiple devices or other show commands that [TextFSM parsers support](https://github.com/networktocode/ntc-templates). 

```python
#!/usr/bin/python3
from netmiko import ConnectHandler
from getpass import getpass
import json
import csv

if __name__ == "__main__":
    device_dict = {
        "device_type": "cisco_ios_telnet",
        "host": "10.10.20.175",
        "username": "cisco",
        "password": getpass(),
    }

    command = "show ip interface brief"

    with ConnectHandler(**device_dict) as net_connect:
        print(net_connect.find_prompt())
        output = net_connect.send_command(command)
        print(output)
        output_fsm = net_connect.send_command(
            command, use_textfsm=True
        )
        print(json.dumps(output_fsm, indent=4))

    csv_columns = ["intf", "ipaddr", "status", "proto"]
    csv_file = "sh_ip_int_fsm.csv"
    try:
        with open(csv_file, "w") as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=csv_columns
            )
            writer.writeheader()
            for data in output_fsm:
                writer.writerow(data)
    except IOError:
        print("I/O error")

```


A couple of things to note:
    - I used the Python `with` statement this time on the `ConnectHandler` instantiation of the Netmiko device object. This means that it will automatically behind the scenes open a connection to the device and then after that indented block is over, close the connection.
    - I chose to use TextFSM templates because they map pretty easily to CSV files. If you chose TTP or Genie parsers, which are also supported by Netmiko, you could achieve the same result.
    - The CSV columns are hard coded in this example, but if you were sending multiple commands and creating multiple CSV files, you would want to make it a variable based on the dictionary keys of the nested object. 
    - I used the JSON library to print out the nested data object instead of something like pprint, which would work also. JSON can be used for quick testing in printing out nested objects by using the `json.dumps` function and a small indentation like I used.  

## Third Script: 3-netmiko-argparse.py

This script is a tool to expose Netmiko functionality in a repeatable and flexible format, a CLI tool. The CLI will prompt the user for a password if one is not given and allows the user to send a command from a selected list. This was a design choice since if the script was shared with a more junior engineer, it gives them an enumerated list to choose from and limits the accidental damage that can be done by sending the wrong commands. I chose the `Argparse` library because it is part of the Python standard library and in my experience large enterprises use bastion jump hosts to house these types of scripts and often have limited access to install new libraries.

The script will send the commands to the device and then if a filename is provided it will write the output to the file. You could easily adapt this to include the code from the second script, where you have TextFSM parsers feed into a CSV file, but I wanted to show something different here, as a junior engineer is probably more at home looking at raw operational data output rather than a CSV file.




```python
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
```

Some things to note:
    - Even though this is just a demo script, I wanted to include help descriptions for each input and a usage blurb to lead by example. It is so important for both your own sanity and helping those who use your script to have self-documenting code.
    - If you wanted to build upon this example another possible direction is prompting the user for a filename input. This would make it easier for engineers to incorporate it into their workflow for larger changes. Asking the user for a CSV file or TXT file of hostnames / IP addresses would add some complexity on the code side, but a big help to the average user.
    - All three of these scripts are read-only by design. It is important to get your confidence up and for your team to trust the tools before doing things like making configuration changes using automation that might break the network.