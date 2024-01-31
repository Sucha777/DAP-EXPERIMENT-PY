def cumulative_sum(input_list):
    cum_sum = 0
    result = []

    for num in input_list:
        cum_sum += num
        result.append(cum_sum)

    return result

# Example usage
user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

cumulative_sum_list = cumulative_sum(user_list)

print("Cumulative sum of the list:", cumulative_sum_list)