# Example list of tuples
tuple_list = [(1, 5), (2, 3), (3, 8), (4, 1), (5, 6)]

# Sort the list of tuples by the second item
sorted_list = sorted(tuple_list, key=lambda x: x[1])

# Display the result
print("Sorted list of tuples by the second item:", sorted_list)
