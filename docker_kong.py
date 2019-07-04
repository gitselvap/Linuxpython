#!/usr/bin/env python

import subprocess

subprocess.call("docker ps | grep kong",shell=True)

