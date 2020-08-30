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

#to change the amount of VLANs change the value of x
#for example to create VLANs ranging from 11-20
#set loop as for x in range (11,21)
for x in range (2,11):
        print "Creating VLAN " + str(x)
        remote_connection.send("vlan " + str(x) + "\n")
        v_name = raw_input("Enter VLAN name: ")
        remote_connection.send("name " + v_name + "\n")
        time.sleep(0.5)

remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output

ssh_client.close