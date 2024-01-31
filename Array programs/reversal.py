# Program for Reversal algorithm for array rotation
def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array_reversal(arr, k):
    k = k % len(arr)
    reverse_array(arr, 0, k - 1)
    reverse_array(arr, k, len(arr) - 1)
    reverse_array(arr, 0, len(arr) - 1)
    return arr

# Example usage:
array = [1, 2, 3, 4, 5]
rotation_steps = int(input("Enter the number of rotation steps: "))
result = rotate_array_reversal(array, rotation_steps)
print("Array after rotation:", result)
