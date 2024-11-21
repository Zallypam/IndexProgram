# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:17:20 2024

@author: ADMIN
"""

# empty list creation
my_list = []

# append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position
my_list.insert(1, 15)

# Extend list with another list
my_list.extend([50, 60, 70])

# Remove last element from the list
my_list.pop()

#Sort list in ascending order
my_list.sort()

#  Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)


