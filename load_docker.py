#!/usr/bin/env python

import subprocess
import time
import sys
import os

Build=(sys.argv[1])
'''
subprocess.call("docker stop sure-ui",shell=True)
time.sleep(5)

print("\nDOCKER SURE_UI STOPPED SUCCESSFULLY")

subprocess.call("docker rm sure-ui",shell=True)
time.sleep(5)

print("\nDOCKER SURE_UI REMOVED SUCCESSFULLY")

subprocess.call("docker rmi sure-ui:18.10",shell=True)
time.sleep(10)

print("\nDOCKER SURE_UI IMAGE REMOVED SUCCESSFULLY")

'''

print("\nPRIVATE SURE-UI DOCKER IMAGE DOWNLOADING UNDER PROCESS\n")
print("\nPROCESSING##########\n")


f = open('logfile.txt', 'w')
path="/root/sure_docker_images"
os.chdir(path)


out=os.system('wget  https://repo.lab.pl.alcatel-lucent.com/sure-mvn-candidates/SURE_UI_PORTAL/'+ Build +'/SURE_R18.10_SUREUI_DOCKER.tar.gz > /dev/null 2>&1')

print("\nPROCESSING#######################################\n")
time.sleep(5)


print("\nDOCKER SURE_UI DOWNLOADED SUCCESSFULLY\n")

print("\nSURE-UI DOCKER TAR EXTRACTING UNDER PROCESS\n") 

tar=os.system('tar -zxvf SURE_R18.10_SUREUI_DOCKER.tar.gz >/dev/null 2>&1')

time.sleep(2)

print("\nDOCKER SURE_UI EXTRACTION COMPLETED SUCCESSFULLY\n")

#wget --user=jenkins  --password=jenkins https://repo.lab.pl.alcatel-lucent.com/sure-mvn-candidates/SURE_UI_PORTAL/Build/SURE_R18.10_SUREUI_DOCKER.tar.gz
#subprocess.call("docker ps -a",shell=True)
#subprocess.call("docker ps -a -q",shell=True)

'''
print("\nSURE_UI DOCKER WILL BE LOADED SHORTLY####\n")

subprocess.call("docker load -i sure-ui_18.10.tar",shell=True)

print("\nDOCKER SURE_UI TAR LOADED SUCCESSFULLY\n")


print("\nSURE_UI PORTAL DOCKER-COMPOSE WILL BE STARTED SHORTLY####\n")

compose="/opt/sure_deployment/"
os.chdir(compose)

subprocess.call("docker-compose -f docker-compose-sure-portal.yml up -d",shell=True)

print("\nDOCKER SURE_UI PORTAL STARTED SUCCESSFULLY")
'''

