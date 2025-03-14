N = 9
M = 9
a = []
for rows in range(N):
    rows = list(map(int,input().split()))
    a.append(rows)
    

max_value = -1
max_location = (0,0)

for rows in range(N):
    for columns in range(N):
        if a[rows][columns] > max_value:
            max_value = a[rows][columns]
            max_location = (rows+1,columns+1)



print(max_value)
print(max_location[0],max_location[1])




