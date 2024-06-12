#!/usr/bin/env python3

import os
import subprocess

ls_return = os.popen('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.popen('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.popen('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return)

p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)