#!/usr/bin/env python3
#AUthor ID: yzabala@myseneca.ca

import subprocess

def free_space():
    process = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    stdout = output.decode('utf-8').strip()
    
    return stdout

if __name__ == "__main__":
    print(free_space())