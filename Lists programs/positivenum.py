user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

positive_num = [num for num in user_list if num >= 0]

print("The positive number in the list  are:", positive_num)