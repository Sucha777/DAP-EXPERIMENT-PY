user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

largest_element = max(user_list)
print("The largest of all elements is:", largest_element)