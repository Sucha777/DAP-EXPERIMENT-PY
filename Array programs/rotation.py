# Program for array rotation
def rotate_array(arr, k):
    k = k % len(arr)
    return arr[k:] + arr[:k]

# Example usage:
array = [1, 2, 3, 4, 5]
rotation_steps = int(input("Enter the number of rotation steps: "))
result = rotate_array(array, rotation_steps)
print("Array after rotation:", result)
