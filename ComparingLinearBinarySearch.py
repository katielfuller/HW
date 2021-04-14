# File: ComparingLinearBinarySearch.py
# Student:
# UT EID:
# Course Name: CS303E
#
# Date Created:
# Date Last Modified:
# Description of Program:

def linearSearch( lst, key ):
    """
    Search for key in unsorted list lst.  Note that
    the index + 1 is also the number of probes.
    """
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def keys2find(quantity):
    """
    This method will generate a list of random selected values from 0 to 999
    The number (quantity) of number that are in the list will be determined
    by the passed in variable quantity.
    e.g if quantity is 10 then a list will be returned with 10 random number
    each between the range maval (999) to minval (0)
    """
    maxval = 999
    minval = 0
    item_list = []
    for x in range(quantity):
        item_list.append(random.randint(minval,maxval))
    return item_list

#################################################################################
##  Main Program starts here.
#   Methods to support the main program are place above this section
#################################################################################

# import required packages
import random

# Remember that range does not include the final value.  To get 999 in the list we must use 1000 in the range function
search_list = list(range(0, 1000, 1))
#print(f'The orignial list is:\n{search_list}')
random.shuffle(search_list)
#print(f'The shuffled list is:\n{search_list}')


num2find = random.randint(0,999)
print(f'In this pass we will search for the randomly chosen value {num2find}')

probes_linear = linearSearch( search_list, num2find)
print(f'To find the number {num2find} in the list took {probes_linear} iterations')

tooFind = keys2find(10)
print(f'The numbers that will be looked for are {tooFind}')
#can I do something like this?
numbers = list(range(1000))
print(f'Your numbers before the shuffle are {numbers}')
random.shuffle(numbers)
print(f'Your numbers after the shuffle are {numbers}')
count1 = 0
count2 = 0

# My first thoughts.  Do you see how nearly the same code is repeated on multiple lines.
# One should try to avoid this.  When you have something like this it is probably a good idea to
# turn it into some sort of method (or at least a loop)
# I also noticed that you code did not run.  Use print statements to ensure you code is running
# Make notes in your code about what the variable is and what you are using it for

# Create a list that represent the five trial sizes that are expected to be evaluated.
# The first trial will search for 10 numbers and the second trial will search for 100, etc
tests = [10,  100, 1000, 10000, 100000]
for test in tests:
    print(f'Run this trial with {test} searches being performed')

# A note about what you are doing here.  Note that in you calling of the linearSearch method you rae passing just one
# variable "numbers"
# But the method requires two inputs   (linearSearch( lst, key ):
#for i in range(1, 10):
#    (count1 += linearSearch(numbers)) / 10
#for i in range(1, 100):
#    (count2 += linearSearch(numbers)) / 100
#for i in range(1, 1000):
#    (count1 += linearSearch(numbers)) / 1000
#for i in range(1, 10000):
#    (count2 += linearSearch(numbers)) / 10000
#for i in range(1, 100000):
#    (count2 += linearSearch(numbers)) / 100000

