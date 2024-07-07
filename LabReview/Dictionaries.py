#!/usr/bin/env python3

dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Postal Code': 'M3J3M6', 'Province': 'ON'}

print(dict_york.values())

print(dict_york.keys())

print(dict_york['Address'])

print(dict_york['Postal Code'])

""" Add key and value """
dict_york['Country'] = 'Canada'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

""" Change key value """
dict_york['Province'] = 'BC'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

list_of_keys = list(dict_york.keys())
print(list_of_keys[0])