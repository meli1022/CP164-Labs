"""
------------------------------------------------------------------------
Task 6
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-01-15"
------------------------------------------------------------------------
"""
import Food_utilities

file_variable = open("new_foods.txt", "w")

fv = open("foods.txt", "r")

foods = Food_utilities.read_foods(fv)



Food_utilities.write_foods(file_variable, foods)






