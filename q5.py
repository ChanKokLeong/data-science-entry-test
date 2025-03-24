Task 1
# Create a function to check if the number (num) is divisible by another number (divisor).
# Both num and divisor must be numeric.
# Return True if num is divisible by divisor, False otherwise.

def check_divisibility(num, divisor):    # define function to check divisibility of 2 nunmbers
    
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):  # check if both numbers are numeric
        raise ValueError("Both num and divisor must be numeric.")
    
    return num % divisor == 0  # check divisibility and return True if divisible and False otherwise



Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

result = check_divisibility(10, 2)
print(result)

result = check_divisibility(7, 3)
print(result)

