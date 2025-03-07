X = int(input())
N = int(input())
sum = 0
for i in range(N):
    a,b = map(int,input().split())
    result = a*b
    sum += result#result = result + i


if X == sum:
    print("Yes")
else:
    print("No")