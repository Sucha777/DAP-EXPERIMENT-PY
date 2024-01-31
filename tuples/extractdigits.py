def extract_digits_from_tuples(tuple_list):
    result = []

    for tpl in tuple_list:
        extracted_digits = ''.join(filter(str.isdigit, str(tpl)))
        result.append(int(extracted_digits))

    return result

# Example list of tuples
tuple_list = [(1, 'abc', 23), ('xyz', 456, '789'), (99, 'pqr', '123')]

# Extract digits from tuples
result_digits = extract_digits_from_tuples(tuple_list)

# Display the result
print("Extracted digits from tuples:", result_digits)
