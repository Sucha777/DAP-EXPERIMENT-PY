num = int(input("Enter a number:"))
sum = 0
order = len(str(num))
copy_num = num
while(num>0):
    digit = num%10
    sum += digit **order
    num = num//10
if(sum == copy_num):
 print("Num is an armstrong number",num)
else:
  print("Num is not an armstrong number",num)