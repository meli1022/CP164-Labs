"""
------------------------------------------------------------------------
Task 2
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-22"
------------------------------------------------------------------------
"""
import utilities 
from Stack_array import Stack


source = [11, 22, 33, 44, 55, 66]
stack = Stack()

utilities.array_to_stack(stack, source)

print(stack)