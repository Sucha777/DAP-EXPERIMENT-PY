
# Example lists
list1 = [4, 2, 1, 3]
list2 = ['apple', 'banana', 'orange', 'grape']

# Sort list1 based on the values of list2
sorted_lists = sorted(zip(list2, list1))
result_list1 = [item[1] for item in sorted_lists]

# Display the result
print("Original list1:", list1)
print("Original list2:", list2)
print("Sorted list1 based on list2 values:", result_list1)