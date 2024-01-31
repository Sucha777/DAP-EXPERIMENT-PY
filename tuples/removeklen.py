def remove_tuples_of_length_k(tuple_list, K):
    return [tpl for tpl in tuple_list if len(tpl) != K]

# Example list of tuples
tuple_list = [(1, 2, 3), ('a', 'b'), (4, 5, 6, 7), ('x', 'y', 'z')]

# Specify the length K to remove
K = 3

# Remove tuples of length K
result_list = remove_tuples_of_length_k(tuple_list, K)

# Display the result
print("List after removing tuples of length", K, ":", result_list)
