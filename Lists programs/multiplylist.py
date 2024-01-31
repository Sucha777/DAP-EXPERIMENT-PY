user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

product = 1
for num in user_list:
    product *= num

print("The multiply of all elements is:", product)