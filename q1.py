To create a function that would swap the value of x and y using only x and y as numeric. If one or both values are not numeric the function to return -1 and print the result that one or both values are not numeric.
def swap(x, y): # define function to swap values x and y
  if not (isinstance(x, (int, float) and y, (int, float))):  # check if both values x and y are numeric
    return -1  # if one or both values are not numeric return -1

x, y = y, x

print(f'(Swapped value: x = {x}, y = {y}')
return x, y

result = swap(9, 21)  # example of both values are numeric 
if result == -1:

result = swap('Bus', 21)  # example of one value not numeric
if result == -1:
  print('One or both values are not numeric') 
