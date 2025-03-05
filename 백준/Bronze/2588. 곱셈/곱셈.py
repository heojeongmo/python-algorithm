n = int(input())
y = int(input())
print(n*(y%10))
print(n*((y//10)%10))
print(n*((y//100)%10))
print(n*y)

