import heapq

def max_min_k_elements(my_tuple, k):
    # Use heapq to find the K largest and smallest elements
    max_elements = heapq.nlargest(k, my_tuple)
    min_elements = heapq.nsmallest(k, my_tuple)

    return max_elements, min_elements

# Example tuple
example_tuple = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

# Specify the value of K
K = 3

# Find the maximum and minimum K elements in the tuple
max_elements, min_elements = max_min_k_elements(example_tuple, K)

# Display the result
print(f"The {K} largest elements in the tuple:", max_elements)
print(f"The {K} smallest elements in the tuple:", min_elements)
