# 문제를 풀 당시 생각 과정을 기입
'''
1부터 시작 스위치
1은 켜짐 0은 꺼짐

남학생 스위치 번호가 자기 번호의 배수면  스위치 상태를 바끔
여학생 자기 번호와 같은 번호 스위치 중심 좌우 대칭이면서 가장 많은 스위치를 포함하는 구간 찾아 상태를 모두 바꿈
= 여학생 3번이면 3번 중심 2번 4번이 둘다 0 1번 5번이 둘다 1이면 1~5 다 상태 바꿈 만약 3번 5번 상태가 다르면 4번만 바꿈
배수들만 반적 시키는 방법과 좌우 대칭이 되는 최대 범위를 찾아야함
'''

# 풀이 코드 기입
n = int(input())
man = []
mannum = []
switch = list(map(int,input().split()))

students = int(input())

for i in range(students):
    x , y = map(int,input().split())
    man.append(x)
    mannum.append(y)

for j in range(students):
    if man[j] == 1:
        for k in range(mannum[j] -1 ,n ,mannum[j] ):
            if k % mannum[k]==0:
                if switch[k] == 1:
                    switch[k] = 0
                else:
                    switch[k] = 1
    elif man[j] == 2:
        for k in range(switch):
            if k == mannum[k] :
                if mannum[k-1] == mannum[k+1]:
                    switch[k] = 1



##########################################
n = int(input())  # 스위치의 개수
switch = list(map(int, input().split()))  # 스위치 상태

students = int(input())  # 학생 수
man = []
mannum = []

for i in range(students):
    x, y = map(int, input().split())
    man.append(x)
    mannum.append(y)

for j in range(students):
    if man[j] == 1:  # 남학생인 경우
        for k in range(mannum[j] - 1, n, mannum[j]):
            switch[k] = 1 - switch[k]  # 스위치 상태 반전

    elif man[j] == 2:  # 여학생인 경우
        idx = mannum[j] - 1
        left = right = idx

        while left >= 0 and right < n and switch[left] == switch[right]:
            switch[left] = 1 - switch[left]
            if left != right:
                switch[right] = 1 - switch[right]
            left -= 1
            right += 1

# 스위치 상태를 20개씩 출력
for i in range(0, n, 20):
    print(*switch[i:i + 20])

# 피드백 후 정리(알게된 점, 포인트 등)
'''
배수들만 반적 시키는 방법과 좌우 대칭이 되는 최대 범위를 찾아야함
switch[k] = 1 - switch[k]  # 스위치 상태 반전시키기 위해 1-1 =0 1-0=1을 이용
left right를 처음엔 여학생 숫자로 지정했다가 여기서 하나씩 증감
반복문을 돌다 특정 조건을 만나면 멈추고 스위치 상태 반전
'''