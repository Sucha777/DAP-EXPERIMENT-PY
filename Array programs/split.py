# Program to split the array and add the first part to the end
def split_and_add(arr, k):
    return arr[k:] + arr[:k]

# Example usage:
array = [1, 2, 3, 4, 5]
split_position = int(input("Enter the split position: "))
result = split_and_add(array, split_position)
print("Array after split and add:", result)
