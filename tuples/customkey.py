# Example nested tuple
nested_tuple = (('a', 1), ('b', 2), ('c', 3))

# Convert nested tuple to a dictionary with custom key
custom_key_dict = {key: value for key, value in nested_tuple}

# Display the result
print("Dictionary with custom key:", custom_key_dict)
