# Program to check if the given array is Monotonic
def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing

# Example usage:
array = [1, 2, 3, 4, 5]
result = is_monotonic(array)
if result:
    print("The array is monotonic.")
else:
    print("The array is not monotonic.")
