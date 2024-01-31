# Sample list with empty lists
original_list = [1, [], 2, [], [], 3, 4, [], 5]

# Remove empty lists using list comprehension
filtered_list = [lst for lst in original_list if lst]

print("Original list:", original_list)
print("List after removing empty lists:", filtered_list)