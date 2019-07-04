#!/usr/bin/env python

import os
import sys

rel=(sys.argv[1])
url = os.path.join('https://repo.lab.pl.alcatel-lucent.com/sure-mvn-candidates/SURE_UI_PORTAL/', rel,'SURE_R18.10_SUREUI_DOCKER.tar.gz')
user=(sys.argv[2])
#pass=(sys.argv[3])
print url

cmd='wget --user=user --password=pass url'
print user

print cmd






