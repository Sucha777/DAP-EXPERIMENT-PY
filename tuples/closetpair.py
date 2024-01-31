def closest_pair_to_kth_element(my_tuple, K):
    target_element = my_tuple[K]
    closest_pair = None
    min_distance = float('inf')

    for i in range(len(my_tuple)):
        if i != K:
            distance = abs(target_element - my_tuple[i])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (target_element, my_tuple[i])

    return closest_pair

# Example tuple
example_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

# Specify the value of K
K = 3

# Find the closest pair to the Kth index element in the tuple
result_pair = closest_pair_to_kth_element(example_tuple, K)

# Display the result
print(f"The closest pair to the Kth index element ({K}) in the tuple:", result_pair)
