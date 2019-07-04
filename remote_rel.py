#!/usr/bin/env python

import subprocess
import paramiko
import sys

#host="135.250.139.106"
host=(sys.argv[1])

user="root"


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, port=22, username=user, password='Nokia@123')
stdin, stdout, stderr = client.exec_command('cat "/opt/sure/release.info" ')

print(repr(stdout))
print(stdout.read())
print("\n")
client.close()

#subprocess.call("docker ps",shell=True)
#subprocess.call("docker ps -a",shell=True)
#subprocess.call("docker ps -a -q",shell=True)

