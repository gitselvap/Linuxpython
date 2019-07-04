#! /usr/bin/env python

import os

import subprocess

path="/root/python/test"

os.chdir(path)

op=subprocess.call("ls -x",shell=True)

#print op

output=str(op)

print output

base=os.path.basename('output')

print base

res=os.path.splitext(base)

print res







