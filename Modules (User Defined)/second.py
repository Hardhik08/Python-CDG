# from first import first
# import math

# first.first("SECOND USER")

# math.fa


def min_max(numbers):
# You have correctly used min and max functions;
# ensure you get input as a list of numbers.
   
    min_value = min(numbers)
    max_value = max(numbers)

    return (min_value, max_value)
numbers = list(map(int, input().split()))
a = min_max(numbers)
print(a)

import os 
import platform

platform.system()