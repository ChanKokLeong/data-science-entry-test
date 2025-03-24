Task-1
# Create a function that searches for all occurences of a value (find_item) in a given list (lst) and replaces with another value (new_value).
# lsr must be a list.
# to Return the modified list

def replace_value(lst, find_item, new_value):  # define function to replace find_item with new_value
  if not isinstance(lst, list):                 # check lst is a list
    raise ValueError('The input "lst" must be a list')

  modified_list = [new_value if item == find_item else item for item in lst]  # modified list with new_value replacing find_item

  return modified_list




Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"


my_list = [1, 2, 3, 4, 2, 2]
find_item = 2
new_value = 5

result = replace_value(my_list, find_item, new_value)
print(result)

my_list = ['apple', 'banana', 'apple']
find_item = 'apple'
new_value = 'orange'

result = replace_value(my_list, find_item, new_value)
print(result)
