def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def sum_of_digits_in_list(input_list):
    result = [sum_of_digits(num) for num in input_list]
    return result

# Example usage
user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

sum_of_digits_list = sum_of_digits_in_list(user_list)

print("Sum of digits in each number:", sum_of_digits_list)