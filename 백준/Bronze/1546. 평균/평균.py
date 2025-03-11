Total_number = int(input())
Score = list(map(int,input().split()))
M = max(Score)
for i in range(Total_number):
    Score[i] = Score[i] / M*100

print(sum(Score)/Total_number)


