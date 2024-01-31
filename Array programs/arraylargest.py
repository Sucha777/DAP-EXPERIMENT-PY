def large(arr, n):
    lar = arr[0]
    for i in range(1,n):
        if lar < arr[i]:
            lar = arr[i]
            return lar

arr = []

n = int(input("Enter n:"))
for i in range(0, n):
    t = int(input())
    arr.append(t)
print(arr)
ans = large(arr, n)
print("The largest element in Array is:",ans)