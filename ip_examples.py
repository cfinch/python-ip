import os
from ip import *

# This file demonstrates how to use the IPAddress class

first_ethernet_IP = "172.20.102.39"
first_infiniband_IP = "172.21.102.39"
first_new_node = 293
last_new_node = 308

# Generate lines for file /etc/hosts

print("Lines to paste into /etc/hosts" + os.linesep)
ethernet_ip = IPAddress(first_ethernet_IP)
for i in range(first_new_node, last_new_node + 1):
    print("{0}   ec{1}    ec{1}.stokes.net".format(ethernet_ip, i))
    ethernet_ip += 1
print("-------------------")

infiniband_ip = IPAddress(first_infiniband_IP) 
for i in range(first_new_node, last_new_node + 1):
    print("{0}   ec{1}    ic{1}.stokes.net".format(infiniband_ip, i))
    infiniband_ip += 1
print("-------------------")

# /etc/hosts.equiv and /etc/ssh/shosts.equiv
print("Lines to paste into /etc/hosts.equiv and /etc/ssh/shosts.equiv" + os.linesep)
ethernet_ip = IPAddress(first_ethernet_IP)
infiniband_ip = IPAddress(first_infiniband_IP) 

for i in range(first_new_node, last_new_node + 1):
    print("{}".format(ethernet_ip))
    print("ec{}".format(i))
    print("{}".format(infiniband_ip))
    print("ic{}".format(i))
    ethernet_ip += 1
    infiniband_ip += 1
print("-------------------")

# /etc/ssh/ssh_known_hosts
print("Lines to paste into /etc/ssh/ssh_known_hosts" + os.linesep)
ethernet_ip = IPAddress(first_ethernet_IP)
infiniband_ip = IPAddress(first_infiniband_IP) 

ec_string = ""
ethernet_ip_string = ""
ic_string = ""
infiniband_ip_string = ""

for i in range(first_new_node, last_new_node + 1):
    ec_string += ",ec{}".format(i)
    ic_string += ",ic{}".format(i)
    ethernet_ip_string += ",{}".format(ethernet_ip)
    infiniband_ip_string += ",{}".format(infiniband_ip)

    ethernet_ip += 1
    infiniband_ip += 1

print ec_string
print ic_string
print ethernet_ip_string
print infiniband_ip_string
print("-------------------")

# DSH node group files
print("Lines to paste into node group files for DSH" + os.linesep)
ethernet_ip = IPAddress(first_ethernet_IP)

for i in range(first_new_node, last_new_node + 1):
    print("ec{}".format(i))
    ethernet_ip += 1
    infiniband_ip += 1
print("-------------------")

# Testing broadcast calculation

# Example from http://en.wikipedia.org/wiki/Broadcast_address
ip = IPAddress('172.16.0.0')
netmask = IPAddress('255.240.0.0')
bc = ip.broadcast(netmask)
print("IP:{}  netmask:{}   broadcast:{}".format(ip, netmask, bc))

# Example from http://en.wikipedia.org/wiki/Broadcast_address
ip = IPAddress('192.168.5.0')
netmask = IPAddress('255.240.0.0')
print(" Address: {}".format(binary(ip)))
print(" Netmask: {}".format(netmask))
print(" Netmask: {}".format(binary(netmask)))
print("~Netmask: {0:032b}".format(complement(binary(netmask))))
bc = ip.broadcast(netmask)
print("IP:{}  netmask:{}   broadcast:{}".format(ip, netmask, bc))

# Example from
ip = IPAddress('132.170.30.3')
netmask = IPAddress('255.255.255.128')
bc = ip.broadcast(netmask)
print("IP:{}  netmask:{}   broadcast:{}".format(ip, netmask, bc))

# Generate netmask from CIDR notation
ip = IPAddress('132.170.30.3')
CIDR = 27
netmask = ip.netmask(CIDR)
bc = ip.broadcast(netmask)
print("IP:{}/{}  netmask:{}   broadcast:{}".format(ip, CIDR, netmask, bc))
