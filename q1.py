Task-1
# To create a function that would swap the value of x and y using only x and y as numeric. 
# If one or both values are not numeric the function to return -1 and print the result that one or both values are not numeric.

def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):  # check if both x and y are numeric
        print("One or both values are not numeric.")
        return -1
    x, y = y, x  # Swap the values
  
    print(f"Swapped value: x = {x}, y = {y}")
  
    return x, y



Task-2
# Invoke the function swap using the following scenarious:
# ('Apple', 10)
# (9, 17)

result = swap('Apple', 10)
if result == -1:
    print('Swap not possible')


result = swap(9, 17)
if result != -1:
    print('Swap possible')
