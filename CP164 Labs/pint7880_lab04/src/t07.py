"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-02-05"
------------------------------------------------------------------------
"""

import utilities
import Food_utilities

file_variable = open("foods.txt", "r")

a = Food_utilities.read_foods(file_variable)

utilities.list_test(a)