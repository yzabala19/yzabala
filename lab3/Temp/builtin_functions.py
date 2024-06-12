#!/usr/bin/env python3

import os

ls_return = os.system('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.system('whoami')
print('The contents of whoami_return:',whoami_return)
ipconfig_return = os.system('ipconfig')
print('The contents of ipconfig_return:',ipconfig_return)
