student = [i for i in range(1,31)] #리스트 컨프리헨션을 사용한다(교실엔 학생이 30명이 있다고 하면 1~30까지 수를 student 리스트에 추가)
for i in range(28): #과제를 제출한 28명의 학생을 입력받아 number에 저장
    number = int(input()) # 과제를 제출한 학생 번호를 입력받아 number에 저장하는 목적이다.
    student.remove(number) # remove를 이용해 student에 있는 수에서 number에 해당하는 수를 삭제한다.


print(min(student))
print(max(student))
