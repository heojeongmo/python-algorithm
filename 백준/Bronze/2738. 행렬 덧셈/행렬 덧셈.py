
N,M = map(int,input().split()) #N은 -> 행 , M은 -> 열열
arr = []
arr1 = []

for row in range(N):
    row = list(map(int,input().split()))
    arr.append(row)

for row in range(N):
    row = list(map(int,input().split()))
    arr1.append(row)

for row in range(N):
    for col in range(M):
        print(arr[row][col]+arr1[row][col], end=' ')
    print()    
        
