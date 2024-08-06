# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
주어진 n이 작다. 출석한 학생인지 확인하면된다.
-> 그냥 선형 탐색 하면 된다고 판단

- 나의 접근에 문제점이 무엇일까 생각해보기

- 시간 복잡도를 고려해보기
for 문 내에서 in을 사용중이므로 O(n^2)이다. 정확히는 O(N*M)

'''

# 풀이 코드 기입
li = []
for i in range(1, 31):
    li.append(i)

attempted = []
for i in range(28):
    attempted.append(int(input()))

for a in li:
    if a not in attempted:
        print(a)