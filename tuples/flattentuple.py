from itertools import chain

# Example tuple of lists
tuple_of_lists = ([1, 2, 3], ['a', 'b', 'c'], [4, 5, 6])

# Flatten the tuple of lists into a single tuple
flattened_tuple = tuple(chain(*tuple_of_lists))

# Display the result
print("Flattened tuple:", flattened_tuple)
