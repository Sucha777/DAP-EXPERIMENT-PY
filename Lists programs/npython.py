def chunks(lst, N):
    return [lst[i:i + N] for i in range(0, len(lst), N)]

# Example usage
user_input = input("Enter elements of the list separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

chunk_size = int(input("Enter the size of each chunk: "))

result_chunks = chunks(user_list, chunk_size)

print(f"List divided into chunks of size {chunk_size}:", result_chunks)
