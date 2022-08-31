# Demo 1: Building your first Netmiko script

Goal: In this demo you will build a CSV report from the outputs of your show commands using TextFSM templates. 

Netmiko Version 4.1.0/4.1.2 requires Python Version 3.7 or higher. 🐍
<https://github.com/ktbyers/netmiko/releases>



### list of device types by giving invalid device type:

(the-u) demo-1$ python 1-netmiko-intro.py
/Users/jabelk/dev/.ve/the-u/lib/python3.6/site-packages/paramiko/transport.py:33: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography and will be removed in a future release.
  from cryptography.hazmat.backends import default_backend
Traceback (most recent call last):
  File "1-netmiko-intro.py", line 13, in <module>
    net_connect = ConnectHandler(**cisco1)
  File "/Users/jabelk/dev/.ve/the-u/lib/python3.6/site-packages/netmiko/ssh_dispatcher.py", line 341, in ConnectHandler
    "currently supported platforms are: {}".format(msg_str)
ValueError: Unsupported 'device_type' currently supported platforms are:
a10
accedian
adtran_os
alcatel_aos
alcatel_sros
allied_telesis_awplus
apresia_aeos
arista_eos
aruba_os
aruba_osswitch
aruba_procurve
avaya_ers
avaya_vsp
broadcom_icos
brocade_fastiron
brocade_fos
brocade_netiron
brocade_nos
brocade_vdx
brocade_vyos
calix_b6
cdot_cros
centec_os
checkpoint_gaia
ciena_saos
cisco_asa
cisco_ftd
cisco_ios
cisco_nxos
cisco_s300
cisco_tp
cisco_viptela
cisco_wlc
cisco_xe
cisco_xr
cloudgenix_ion
coriant
dell_dnos9
dell_force10
dell_isilon
dell_os10
dell_os6
dell_os9
dell_powerconnect
dell_sonic
dlink_ds
eltex
eltex_esr
endace
enterasys
ericsson_ipos
extreme
extreme_ers
extreme_exos
extreme_netiron
extreme_nos
extreme_slx
extreme_tierra
extreme_vdx
extreme_vsp
extreme_wing
f5_linux
f5_ltm
f5_tmsh
flexvnf
fortinet
generic
generic_termserver
hp_comware
hp_procurve
huawei
huawei_olt
huawei_smartax
huawei_vrpv8
ipinfusion_ocnos
juniper
juniper_junos
juniper_screenos
keymile
keymile_nos
linux
mellanox
mellanox_mlnxos
mikrotik_routeros
mikrotik_switchos
mrv_lx
mrv_optiswitch
netapp_cdot
netgear_prosafe
netscaler
nokia_sros
oneaccess_oneos
ovs_linux
paloalto_panos
pluribus
quanta_mesh
rad_etx
raisecom_roap
ruckus_fastiron
ruijie_os
sixwind_os
sophos_sfos
supermicro_smis
tplink_jetstream
ubiquiti_edge
ubiquiti_edgerouter
ubiquiti_edgeswitch
ubiquiti_unifiswitch
vyatta_vyos
vyos
watchguard_fireware
yamaha
zte_zxros
zyxel_os
(the-u) demo-1$


### list of telnet device types by giving invalid_telnet

(the-u) demo-1$ python 1-netmiko-intro.py
/Users/jabelk/dev/.ve/the-u/lib/python3.6/site-packages/paramiko/transport.py:33: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography and will be removed in a future release.
  from cryptography.hazmat.backends import default_backend
Traceback (most recent call last):
  File "1-netmiko-intro.py", line 13, in <module>
    net_connect = ConnectHandler(**cisco1)
  File "/Users/jabelk/dev/.ve/the-u/lib/python3.6/site-packages/netmiko/ssh_dispatcher.py", line 341, in ConnectHandler
    "currently supported platforms are: {}".format(msg_str)
ValueError: Unsupported 'device_type' currently supported platforms are:
adtran_os_telnet
apresia_aeos_telnet
arista_eos_telnet
aruba_procurve_telnet
brocade_fastiron_telnet
brocade_netiron_telnet
calix_b6_telnet
centec_os_telnet
ciena_saos_telnet
cisco_ios_telnet
cisco_s300_telnet
cisco_xr_telnet
dell_dnos6_telnet
dell_powerconnect_telnet
dlink_ds_telnet
extreme_exos_telnet
extreme_netiron_telnet
extreme_telnet
generic_telnet
generic_termserver_telnet
hp_comware_telnet
hp_procurve_telnet
huawei_olt_telnet
huawei_telnet
ipinfusion_ocnos_telnet
juniper_junos_telnet
nokia_sros_telnet
oneaccess_oneos_telnet
paloalto_panos_telnet
rad_etx_telnet
raisecom_telnet
ruckus_fastiron_telnet
ruijie_os_telnet
supermicro_smis_telnet
tplink_jetstream_telnet
yamaha_telnet
zte_zxros_telnet
(the-u) demo-1$


### gave ssh instead of telnet

(the-u) demo-1$ python 1-netmiko-intro.py
/Users/jabelk/dev/.ve/the-u/lib/python3.6/site-packages/paramiko/transport.py:33: CryptographyDeprecationWarning: Python 3.6 is no longer supported by the Python core team. Therefore, support for it is deprecated in cryptography and will be removed in a future release.
  from cryptography.hazmat.backends import default_backend
Traceback (most recent call last):
  File "/Users/jabelk/dev/.ve/the-u/lib/python3.6/site-packages/netmiko/base_connection.py", line 1021, in establish_connection
    self.remote_conn_pre.connect(**ssh_connect_params)
  File "/Users/jabelk/dev/.ve/the-u/lib/python3.6/site-packages/paramiko/client.py", line 368, in connect
    raise NoValidConnectionsError(errors)
paramiko.ssh_exception.NoValidConnectionsError: [Errno None] Unable to connect to port 22 on 10.10.20.175

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "1-netmiko-intro.py", line 13, in <module>
    net_connect = ConnectHandler(**cisco1)
  File "/Users/jabelk/dev/.ve/the-u/lib/python3.6/site-packages/netmiko/ssh_dispatcher.py", line 344, in ConnectHandler
    return ConnectionClass(*args, **kwargs)
  File "/Users/jabelk/dev/.ve/the-u/lib/python3.6/site-packages/netmiko/base_connection.py", line 434, in __init__
    self._open()
  File "/Users/jabelk/dev/.ve/the-u/lib/python3.6/site-packages/netmiko/base_connection.py", line 439, in _open
    self.establish_connection()
  File "/Users/jabelk/dev/.ve/the-u/lib/python3.6/site-packages/netmiko/base_connection.py", line 1043, in establish_connection
    raise NetmikoTimeoutException(msg)
netmiko.exceptions.NetmikoTimeoutException: TCP connection to device failed.

Common causes of this problem are:

1. Incorrect hostname or IP address.
2. Wrong TCP port.
3. Intermediate firewall blocking access.

Device settings: cisco_ios 10.10.20.175:22

(the-u) demo-1$
