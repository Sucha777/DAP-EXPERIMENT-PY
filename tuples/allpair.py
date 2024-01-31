from itertools import product

def all_pair_combinations(tuple1, tuple2):
    return list(product(tuple1, tuple2))

# Example tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

# Generate all pair combinations
result_combinations = all_pair_combinations(tuple1, tuple2)

# Display the result
print("All pair combinations of elements from two tuples:", result_combinations)
