# Assignment I - Python

# Problem 1
sequence = [x for x in range(2000,3200+1) if x%7==0 and x%5!=0]
print(sequence)

# Problem 2
first = input("First name: ")
last = input("Last name: ")
print(last, first)

# Problem 3
import numpy
diameter = 12
V = 4/3 * numpy.pi * (diameter/2)**3