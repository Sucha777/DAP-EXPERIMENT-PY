
user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]


N = int(input("Enter the value of N: "))


if len(user_list) < N:
    print(f"List has fewer than {N} elements. Cannot find {N} largest elements.")
else:

    sorted_list = sorted(user_list, reverse=True)


    N_largest_elements = sorted_list[:N]


    print(f"{N} largest elements in the list:", N_largest_elements)