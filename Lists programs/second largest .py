# Taking user input for the list
user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

# Finding the second largest number in the list
if len(user_list) < 2:
    print("List must have at least two elements.")
else:
    # Sorting the list in descending order
    sorted_list = sorted(user_list, reverse=True)

    # Finding the second largest number
    second_largest = sorted_list[1]

    # Displaying the result
    print("Second largest number in the list:", second_largest)