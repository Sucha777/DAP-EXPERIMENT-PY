start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

# Printing all odd numbers in the range
print("odd numbers in the range:")
for num in range(start, end + 1):
    if num != 0:
        print(num)