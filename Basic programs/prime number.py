num = int(input("Enter a number:"))

for i in range(2,num):
    if num % i == 0:
        print("It is not Prime")
        break
    else:
        print("It is Prime")