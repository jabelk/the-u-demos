from netmiko import ConnectHandler

# Just pick an 'invalid' device_type or invalid_telnet
cisco1 = {
    # device types: https://github.com/ktbyers/netmiko/blob/master/netmiko/ssh_dispatcher.py#L134
    "device_type": "cisco_ios_telnet",
    "host": "10.10.20.175",
    "username": "cisco",
    "password": "cisco"
}
# The above code will output all of the available SSH device types. Switch to 'invalid_telnet' to see 'telnet' device types.

net_connect = ConnectHandler(**cisco1)
print(net_connect.find_prompt())
net_connect.disconnect()
