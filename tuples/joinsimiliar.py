def join_similar_tuples(tuples_list):
    grouped_dict = {}

    # Group tuples with the same initial element
    for tpl in tuples_list:
        initial_element = tpl[0]
        if initial_element in grouped_dict:
            grouped_dict[initial_element].append(tpl)
        else:
            grouped_dict[initial_element] = [tpl]

    # Join tuples with the same initial element
    result_tuples = [tuple(sum(zip(*group), ())) for group in grouped_dict.values()]

    return result_tuples

# Example list of tuples
tuples_list = [(1, 'apple'), (2, 'banana'), (1, 'orange'), (3, 'grape'), (2, 'kiwi')]

# Join tuples with similar initial element
result = join_similar_tuples(tuples_list)

# Display the result
print("Joined Tuples:", result)
