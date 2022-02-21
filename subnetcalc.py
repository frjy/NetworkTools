
#!/usr/bin/env python3
#Code to Calculate hosts and subnets from given IP address 

import ipaddress
import sys

#Creates IP Address class from ipaddress module
IP_Addr = ipaddress.ip_interface(sys.argv[1])

Net_Addr = IP_Addr.network  
pref_len = int(IP_Addr.with_prefixlen.split('/')[1]) #changes output to interger for use later in script
Mask = IP_Addr.with_netmask
wildcard = IP_Addr.hostmask
broadcast_address = Net_Addr.broadcast_address


print('Network Address : ', str(Net_Addr).split('/')[0])
print('Broadcast Address : ' , broadcast_address)
print('CIDR Notation : ', pref_len)
print('Subnet Mask : ', Mask.split('/')[1])
print('Wildcard Mask : ' , wildcard)
print('First IP : ' , list(Net_Addr.hosts())[0])
print('Last IP : ' , list(Net_Addr.hosts())[-1])
print('Hosts : ' , Net_Addr.num_addresses)
print('-Private: ' , IP_Addr.is_private , ' -Link_Local: ', IP_Addr.is_link_local, ' -Global, ', IP_Addr.is_global)

#Block of code is used to find class boundries and set ip_class
if IP_Addr.ip < ipaddress.IPv4Address('126.255.255.255'):
    print('Class: A')
    ip_class = 'A'

elif IP_Addr.ip < ipaddress.IPv4Address('191.255.255.255'):
    print('Class: B')
    ip_class = 'B'

elif IP_Addr.ip < ipaddress.IPv4Address('223.255.255.255'):
    print('Class: C')
    ip_class = 'C'


print('\nSubnet break down:')

#Loop through smaller subnets and print out hosts and subnets or supernets depending on class
for i in range(pref_len + 1  , 31):
    
    if ip_class == 'A':
        subnets = 2 ** (i - pref_len)
        if i < 8: 
            print('/', i, ' = ' , subnets , 'SuperNets')
        else:
            hosts = 2 ** (32 - i) - 2
            print('/', i, ' = ' , subnets , 'Subenets  and ', hosts, ' Hosts')
    
    elif ip_class == 'B':
        subnets = 2 ** (i - pref_len)
        if i < 16:
            print('/', i, ' = ' , subnets , 'SuperNets')
        else:
            hosts = 2 ** (32 - i) - 2
            print('/', i, ' = ' , subnets , 'Subenets  and ', hosts, ' Hosts')

    elif ip_class == 'C':
        subnets = 2 ** (i - pref_len)
        if i < 24:
            print('/', i, ' = ' , subnets , 'SuperNets')
        else:
            hosts = 2 ** (32 - i) - 2
            print('/', i, ' = ' , subnets , 'Subenets  and ', hosts, ' Hosts')

    else: 
        print('!!! Warning Class D or E IPs !!!')
        subnets = 2 ** (i - pref_len)
        hosts = 2 ** (32 - i) - 2
        print('/', i, ' = ' , subnets , 'Subenets  and ', hosts, ' Hosts')