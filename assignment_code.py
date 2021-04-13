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

