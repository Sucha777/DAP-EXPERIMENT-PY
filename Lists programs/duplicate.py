def find_duplicates(input_list):
    duplicates = []
    seen = set()

    for num in input_list:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates

# Example usage
user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

duplicate_elements = find_duplicates(user_list)

if duplicate_elements:
    print("Duplicate elements in the list:", duplicate_elements)
else:
    print("No duplicate elements found in the list.")

