#! python

import os

mytestfile = '/Users/lanzaaz/MyPythonVirtualEnvironments/TEST/mytestfile'

with open(mytestfile, 'r') as f:
  for device in f.readlines():
    print('Pinging ' + device)
    os.system("ping -c 1 " + device)
