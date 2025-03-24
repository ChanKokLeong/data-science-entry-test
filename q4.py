Task-1
# Create a function that reverses a given string (s).
# s must be a string.
# Return the reversed string.

def reverse_string(s):          # define function to reverse a string (s)
    if not isinstance(s, str):  # check if (s) is a string
        raise TypeError('Input must be a string')
    return s[::-1]              # performs reverse sequence on the string


Task-2
Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

s = 'Hello World'
result = reverse_string(s)
print(result)

s = 'Python'
result = reverse_string(s)
print(result)
