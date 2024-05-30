#!/usr/bin/env python3

import sys

if sys.argv != 2:
    print('You must enter two arguments with your script')
    sys.exit()
     
print(sys.argv[0])
print('The first argument is: ' + sys.argv[1])
print('The second argument is: ' + sys.argv[2])