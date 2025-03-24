def find_first_negative(lst):
    """
Task 1
# Create a function that finds the first negative number in a list (lst).
# Return the first negative number if found, otherwise return "No negatives".
# Use a while loop to implement this.

def find_first_negative(lst):    # define function to find first negative number in a list (lst)
    
    index = 0    # initialize an index variable
    
    while index < len(lst):  # use w while loop to itierate through the list
        
        if lst[index] < 0:  # check if the current element is negative
        
            return lst[index]  # Return the first negative number
        
        index += 1  # increment the index to check the next elementlst
    
    return "No negatives"  # if the loop ends and no negative number is found, return "No negatives"




Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

lst = [3, 5, -1, 7, -2, 8]
result = find_first_negative(lst)
print(result)

lst = [2, 10, 7, 0]
result = find_first_negative(lst)
print(result)
