#!/usr/bin/env python

import subprocess
import time
import sys
import os

subprocess.call("docker stop $(docker ps -a -q)",shell=True)
time.sleep(5)

print("\nDOCKER CONATAINERS STOPPED SUCCESSFULLY")

subprocess.call("docker rm $(docker ps -a -q)",shell=True)
time.sleep(5)

print("\nDOCKER CONATAINERS REMOVED SUCCESSFULLY")

subprocess.call("docker rmi -f $(docker image ls -q)",shell=True)
time.sleep(10)

print("\nDOCKER IMAGES REMOVED SUCCESSFULLY")


