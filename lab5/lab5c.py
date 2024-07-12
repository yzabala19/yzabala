#!/usr/bin/env python3
# Author ID: yzabala-pellicer@myseneca.ca

def add(number1, number2):
    # Add two numbers together, return the result, if error return string 'error: could not add numbers'
    try:
        if isinstance(number1, str) and number1.isdigit():
            number1 = int(number1)
        if isinstance(number2, str) and number2.isdigit():
            number2 = int(number2)
        return number1 + number2
    except TypeError:
        return 'error: could not add numbers'
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    # Read a file, return a list of all lines, if error return string 'error: could not read file'
    try:
        f = open(filename, 'r')
        lines = []
        for line in f.readlines():
            lines.append(line)
        f.close()
        return lines
    except FileNotFoundError:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # works
    print(add('10',5))                      # works
    print(add('abc',5))                     # exception
    print(read_file('seneca2.txt'))         # works
    print(read_file('file10000.txt'))       # exception