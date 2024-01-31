user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

even_elements = [num for num in user_list if num % 2 == 0]

print("The even element in the list  is:", even_elements)