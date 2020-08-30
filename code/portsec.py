#!/usr/bin/env python

import paramiko
import time
from sys import argv

script, ip = argv

ip_address = ip
username = raw_input("Enter username: ")
password = raw_input("Enter password: ")

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print ("SSH connection successful to ", ip_address)

remote_connection = ssh_client.invoke_shell()
remote_connection.send("configure terminal\n")

print "Implementing Port Security " + str(x)
#change interface naming as required
remote_connection.send("interface range GigabitEthernet  2/0-1\n")
remote_connection.send("shutdown\n")
print ("Shutting down unused port\n")

#the number of ports can also be changed by changing the values in the loop
#change interface name as required.
#port security violation can also be changed
for x in range (0,4):
        remote_connection.send("interface range GigabitEthernet 0/" + str(x) + "\n")
        remote_connection.send("switchport mode access\n")
        remote_connection.send("switchport port-security\n")
        remote_connection.send("switchport port-security mac-address sticky\n")
        remote_connection.send("switchport port_security maximum 2\n")
        remote_connection.send("switchport port-security violation shutdown\n")
        time.sleep(0.5)


remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output

ssh_client.close
