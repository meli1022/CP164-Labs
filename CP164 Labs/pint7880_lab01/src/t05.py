"""
------------------------------------------------------------------------
Task 5
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-15"
------------------------------------------------------------------------
"""
import Food_utilities


file_variable = open("foods.txt", "r")

f = Food_utilities.read_foods(file_variable)

print(f)