# Program to find the remainder of array multiplication divided by n
def remainder_of_array_multiplication(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

# Example usage:
array = [2, 3, 4, 5]
modulus = int(input("Enter the value of n: "))
result = remainder_of_array_multiplication(array, modulus)
print("Remainder of array multiplication divided by", modulus, "is:", result)
