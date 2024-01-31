from operator import itemgetter

# Example list of tuples
tuple_list = [(1, 'apple'), (3, 'orange'), (2, 'banana'), (4, 'grape')]

# External list of indices to order tuples
order_indices = [2, 0, 1, 3]

# Order tuples based on the external list of indices
ordered_list = sorted(tuple_list, key=itemgetter(*order_indices))

# Display the result
print("Ordered list of tuples based on external list of indices:", ordered_list)
