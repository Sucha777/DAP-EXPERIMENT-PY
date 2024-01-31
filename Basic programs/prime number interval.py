lower_num = int(input("Enter a lower number:"))
upper_num = int(input("Enter a upper number:"))

for num in range(lower_num, upper_num +1):
  if num > 1:
    for i in range (2,num):
      if num%i == 0:
         break
    else:
       print(num)