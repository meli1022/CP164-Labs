"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-02-24"
------------------------------------------------------------------------
"""

from List_linked import List

test_list = []

test_list2 = []

test_list3 = []

self = List()

value = 2

List.prepend(self, value)

for j in self:
    test_list.append(j)

print("Prepend Test:", test_list)
    
List.append(self, value)

for p in self:
    test_list2.append(p)
print("Append Test:", test_list2)

print("Length of current list",p)

i = 1

List.insert(self, i, value)

for j in self:
    test_list3.append(j)
print("Insert Test:", test_list3)

key = 2

x,y,z = List._linear_search(self, key)

print(x,y,z)








