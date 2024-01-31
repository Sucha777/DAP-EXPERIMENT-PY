# method 1

tuple = (2,3,4,5,'a','c','d')
total_size = len(tuple)
print("size", total_size)

# method 2

user_input = input("Enter elements: ")
user_tuple = [int(x) for x in user_input.split()]
total_size = len(tuple)
print("size", total_size)