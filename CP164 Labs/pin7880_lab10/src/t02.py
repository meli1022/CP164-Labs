"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Melissa Pinto
ID:     190647880
Email:  pint7880@mylaurier.ca
__updated__ = "2020-03-31"
------------------------------------------------------------------------
"""
from test_Sorts_array import test_sort, SORTS

for sort in SORTS:
    test_sort(sort[0], sort[1])