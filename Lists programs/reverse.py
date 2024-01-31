
user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

reversed_list = user_list[::-1]
print("The reversed list of all elements is:", reversed_list)