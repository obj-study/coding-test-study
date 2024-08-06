# 문제를 풀 당시 생각 과정을 기입
'''
m 교수
30명의 학생 1~30
28명만 제출 2명 안함
먼저 28명의 학생을 담을 배열 만들어 추가
정렬하고 다시 1~30까지 for문 돌면서
배열안에 j값이 없으면 제출안한 학생에게 추가
프린트
'''

# 풀이 코드 기입
n = 28
a= []
no =[]
for i in range(n):
    a.append(int(input()))

a.sort()
for j in range(1,31):
    if(j not in a):
      no.append(j)

print(min(no))
print(max(no))

# 피드백 후 정리(알게된 점, 포인트 등)
'''

'''