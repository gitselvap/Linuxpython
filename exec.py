#!/usr/bin/env python

import subprocess
import os

path='/opt/dbdata/databases'

os.chdir(path)

cmd1 ='cypher-shell -uneo4j -padmin@123 -a `hostname` --format verbose < servicestopology.cy.Robi6-services1 > servicestopology.cy.Robi6-services2.log2'

cmd2='cypher-shell -uneo4j -padmin@123 -a `hostname` --format verbose < servicestopology.cy.Robi6-services2 > servicestopology.cy.Robi6-services2.log2'

cmd3='cypher-shell -uneo4j -padmin@123 -a `hostname` --format verbose < servicestopology.cy.Robi6-services3 > servicestopology.cy.Robi6-services3.log3'

#subprocess.call("ping 135.250.139.106 -c 4",shell=True)
#subprocess.call("ls -lr",shell=True)
subprocess.call(cmd,shell=True)


