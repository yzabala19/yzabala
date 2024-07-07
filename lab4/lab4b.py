#!/usr/bin/env python3
# Author ID: yzabala-pellicer@myseneca.ca

def join_lists(l1, l2):
    # join_lists will return a list that contains every value from both l1 and l2
    set1 = set(l1)
    set2 = set(l2)
    return list(set1.union(set2))

def match_lists(l1, l2):
    # match_lists will return a list that contains all values found in both l1 and l2
    temporary_set = set(l1).intersection(set(l2))
    new_list = list(temporary_set) 
    return new_list

def diff_lists(l1, l2):
    # diff_lists will return a list that contains all different values, which are not shared between the lists
    temporary_set = set(l1).symmetric_difference(set(l2))
    new_list = list(temporary_set) 
    return new_list

if __name__ == '__main__':
    list1 = list(range(1,10))
    list2 = list(range(5,15))
    print('list1: ', list1)
    print('list2: ', list2)
    print('join: ', join_lists(list1, list2))
    print('match: ', match_lists(list1, list2))
    print('diff: ', diff_lists(list1, list2))