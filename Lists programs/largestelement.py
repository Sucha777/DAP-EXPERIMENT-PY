list = []
num = int(input("Enter the number of elements in a list:"))
for i in range(1, num+1):
    elements = int(input("Enter elements:"))
    list.append(elements)
print("The elements in a list:", list)
print("The largest element is:", max(list))