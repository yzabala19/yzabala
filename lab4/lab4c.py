#!/usr/bin/env python3
# Author ID: yzabala-pellicer@myseneca.ca

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
    dict = {}
    for index, value in enumerate(keys):
        dict[value] = values[index]
    return dict

def shared_values(dict1, dict2):
    # Place code here - refer to function specifics in section below
    final_list = []
    list_of_keys_1 = list(dict1.keys())
    list_of_keys_2 = list(dict2.keys())
    for key in list_of_keys_1:
        if key in list_of_keys_2 and dict1[key] == dict2[key]:
            final_list.append(dict1[key])

    return set(final_list)



if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)