#!/usr/bin/env python

import subprocess
import os
import sys

var=raw_input("Enter the img: ")
#var=str(sys.argv[1:])
process=os.system('docker ps | grep '+var)


#output=subprocess.call("docker ps | grep [var]",shell=True)
#output=subprocess.call("docker ps",shell=True)
print process

