#!/usr/bin/env python3

shoeSize = ''

while not shoeSize.isdigit():
    shoeSize = input('Provide your Shoe Size: ')
    if shoeSize.isdigit():
        shoeSize = int(shoeSize)
        if shoeSize < 1 or shoeSize > 20:
            shoeSize = ''
        else:
            shoeSize = str(shoeSize)

print('Your shoe size is: ' + shoeSize)

        
