# Demo 1: Building your first Netmiko scripts

Goal: Use Netmiko read-only show commands to get operational data and build a CLI tool to scale it to share with others.

These examples were built using the [NSO Reservable Sandbox](LINK), not because we are using NSO, it just has a nice topology to use. The network devices have telnet connections exposed in this sandbox, so I used the telnet Netmiko connections. The scripts were run in a local virtual environment with VPN access to the Sandbox. Check out the `requirements.txt` file for which version of Netmiko that was used, though most versions should work.

> Note: These examples use Netmiko 4.0.0 because 4.1.0 and greater require Python 3.7 minimum and my local Python was 3.6. You can use newer version of Netmiko if you have Python 3.7+ installed.

## First Script


