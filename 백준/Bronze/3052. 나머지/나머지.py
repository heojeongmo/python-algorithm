number = []
B = 42
result_1=[]

for i in range(10):
    number.append(int(input()))
    result = number[i] % B
    result_1.append(result)
    

print(len(set(result_1)))

