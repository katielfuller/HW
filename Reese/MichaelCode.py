
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
    The number (quantity) of numbers that are in the list will be determined
    by the passed in variable quantity.
    e.g if quantity is 10 then a list will be returned with 10 random number
    each between the range maxval (999) to minval (0)
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
# This will be the main randomized list that we doe the searching IN.  ONce created it will be not changed (just resused)
# for all of the searches.
search_list = list(range(0, 1000, 1))
#print(f'The orignial list is:\n{search_list}')
random.shuffle(search_list)
#print(f'The shuffled list is:\n{search_list}')

# Create a list that represent the five trial sizes that are expected to be evaluated.
# The first trial will search for 10 numbers and the second trial will search for 100, etc
# Another good practice is to shorten your work durring testing.  For example the total set of trial
# is the 10 through 100000 list.   But that is a lot to do over and over durrring testing.  What I have
# done is commented out that list definition and placed a shorter one that just does the first test
# and the first test is with just 10 elemets bewing searched for
tests = [10,  100, 1000, 10000, 100000]
#tests = [10]
#tests = [10,  100]
for test in tests:
    print(f'Run this trial with {test} searches being performed')
    # Create a list that contains the correct number of random values
    # Please note how I have broken down the task and placed some code into methods that are reusable
    tooFindList = keys2find(test)
    #print(f'The numbers that will be looked for are {tooFindList}')

    # Another thing to note is that the variable tooFind is a list.  And therefore there is another
    # opportunity to loop through these values.

    # Now lets do the linear searches
    totalIterations = 0
    for num2find in tooFindList:
        # Remember that the method we were given the number of searches is stated to be one (1)
        # greater than the returned value
        probes_linear = linearSearch( search_list, num2find) + 1
        totalIterations = totalIterations + probes_linear
        #print(f'To find the number {num2find} in the list took {probes_linear} iterations')

    # Calculate the average number of iterations
    averageIterations = totalIterations / test
    print(f'The average iterations for {test} samples was {averageIterations} iterations\n')
