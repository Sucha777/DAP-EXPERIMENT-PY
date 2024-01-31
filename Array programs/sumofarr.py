lt = []

n = int(input("Enter n:"))
for i in range(0, n+1):
    t = int(input())
    lt.append(t)
sum = 0
for et in lt:
    sum = sum + et
print("result", sum)