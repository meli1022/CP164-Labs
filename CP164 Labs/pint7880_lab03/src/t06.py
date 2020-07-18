"""
------------------------------------------------------------------------
Task 6
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-28"
------------------------------------------------------------------------
"""

import Food_utilities
import utilities

file_variable = open("foods.txt", "r")

a = Food_utilities.read_foods(file_variable)

utilities.queue_test(a)