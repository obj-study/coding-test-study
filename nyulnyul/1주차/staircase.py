# 문제를 풀 당시 생각 과정을 기입
'''
한 걸음은 1~2칸을 올라갈 수 있다.
연속으로 3개를 밟기 불가
마지막은 밟아야 한다.
얻을 수 있는 최댓값
최대 값 = 10+20+25+20 = 75

한계단만 밟기 : 2에서 3으로 가면서 2번 밟은거라 1은 못밟음
두계단을 밟기 : 1번째와 마지막을 제외하고 제약 x

마지막값인 20은 고정으로 받음

'''

# 풀이 코드 기입
n = int(input())
dp = [0] * (n+1)
score = [0] * (n+1)

for i in range(1, n+1):
    score[i] = int(input())

if n==1:
    print(score[1])
    exit()
elif n==2:
    print(sum(score[:3]))
    exit()

dp[1] = score[1]
dp[2] = score[1]+score[2]

for i in range(3,n+1):
    dp[i] = max(dp[i-3] + score[i-1] + score[i] , dp[i-2] + score[i])


print(dp[-1])

# 피드백 후 정리(알게된 점, 포인트 등)
'''
1과 2가 n일경우는 성립 불가하니 불가하게 해야함
두가지 경우의수
1. i번째 계단과 i-1번째 계단이 연속 경우
2. 연속되지 않게 i번째 계단 도착 경우

이에 따른 점화식
dp[i] = dp[i-3] + score[i-1] + score[i]
dp[i] = dp[i-2] + score[i]

dp[i] = max(dp[i-3] + score[i-1] + score[i] , dp[i-2] + score[i])


점화식을 구성하는 방법을 잘 모르겠음
'''