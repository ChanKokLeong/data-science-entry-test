Task 1
# Create a function that updates a dictionary (dct) with a new key-value pair.
# If the key already exists in dct, print the original value, then update its value.
# Return the updated dictionary.

def update_dictionary(dict, key, value):
  if key in dict:
    print(f'Original value for key: "{key}": {dict[key]}')
  dict[key] = value
  return dict


Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26


my_dict = {'name': 'Alice', 'age': 25}
my_dict = update_dictionary(my_dict, 'age', 26)
print(my_dict)
