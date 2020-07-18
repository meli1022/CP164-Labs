"""
------------------------------------------------------------------------
Task 7
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-15"
------------------------------------------------------------------------
"""
import Food_utilities

file_variable = open("foods.txt", "r+")

foods = Food_utilities.read_foods(file_variable)

f = Food_utilities.get_vegetarian(foods)

print(f)