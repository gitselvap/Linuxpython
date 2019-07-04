#!/usr/bin/env python

import subprocess
import time
import sys
import os
import getpass

Build=(sys.argv[1])
#user=(sys.argv[1])
#pwd=getpass.getpass("Enter the password:")



print("\nprivate sure-ui docker images under processing...\n")
print("\nprocessing.........\n")
print("\nprocessing.............................\n")




os.system('wget https://repo.lab.pl.alcatel-lucent.com/sure-mvn-candidates/SURE_UI_PORTAL/'+ Build +'/SURE_R18.10_SUREUI_DOCKER.tar.gz')

time.sleep(5)


print("\nDocker SURE_UI completed")

#subprocess.call("docker ps -a",shell=True)
#subprocess.call("docker ps -a -q",shell=True)

