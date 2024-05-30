#!/usr/bin/env python3

grade = int(input('Enter your mark: '))
if grade <= 20:
    print('Your grade is D')
elif grade >20 and grade <= 40:
    print('YOur grade is C')
elif grade >40 and grade <=70:
    print ('Your grade is B')
else:
    print ('Your grade is A')
