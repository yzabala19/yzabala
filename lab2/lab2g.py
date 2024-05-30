#!/usr/bin/env python3

#Author: Yelianny Zabala
#Author ID: yzabala-pellicer@myseneca.ca
#DateCreated: 2024-05-29
import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])
    
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')

