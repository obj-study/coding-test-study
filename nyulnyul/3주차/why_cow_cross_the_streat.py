# 문제를 풀 당시 생각 과정을 기입
'''
소의 위치를 N번 관찰, 관찰은 소의 번호와 소의 위치로 이뤄짐
소의 번호 1<=x<=10 소의 위치 0 or 1

소의 위치가 바뀐게 몇번인가

먼저 배열로 각 값들을 넣어줌
'''

# 풀이 코드 기입
n = int(input())
x = []
y = []
count =0

for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for j in range(n):
    for k in range(n):
        if x[j] == x[k]:
            if y[j] != y[k]:
                count +=1

print(count)
#########################################3
n = int(input())
last = {}
count = 0

for i in range(n):
    cow, pos = map(int, input().split())
    if cow in last:
        if last[cow] != pos:
            count += 1
    last[cow] = pos
print(count)


# 피드백 후 정리(알게된 점, 포인트 등)
'''
위치를 기억하기 위해 딕셔너리를 사용하면 쉽게 풀리는 내용이었다..
'''