user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]


list_sum = sum(user_list)


print("The total sum of elements are:", list_sum)