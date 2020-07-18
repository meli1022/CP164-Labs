"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-03-26"
------------------------------------------------------------------------
"""
import Food_utilities

import functions

file_variable =  open('foods.txt', 'r')

slots = 7

values = Food_utilities.read_foods(file_variable)

functions.hash_table(slots, values)