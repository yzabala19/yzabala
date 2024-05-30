#!/usr/bin/env python3

print('1. Convert inches -> cm' + '\n' + '2. Convert cm -> inches')
seleccion=input('Make your selection (1,2): ')

if int(seleccion) ==1:
    value = input('Enter inches: ')
    operation = int(value) * 2.54
    print('Number of cm: ' + str(operation))
elif int(seleccion) ==2:
    value = input('Enter cm: ')
    operation = int(value) / 2.54
    print('Number of inches: ' + str(operation))
else:
    print('Invalid Entry ')
    