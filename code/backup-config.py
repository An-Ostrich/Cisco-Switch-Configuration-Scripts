#!/usr/bin/env python

import datetime
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
remote_connection.send("terminal length 0\n")

print ("Getting running configuration...\n")
remote_connection.send("show running-config\n")
time.sleep(10)
remote_connection.send("exit\n")
time.sleep(0.5)
output = remote_connection.recv(65535)

file = 'SW '+str(ip)+" " +  str(datetime.date.today().isoformat())

op_file = open(file,'w')
op_file.write(output.decode("utf-8"))
print ("Writing configuration to file...\n")
op_file.close()

ssh_client.close