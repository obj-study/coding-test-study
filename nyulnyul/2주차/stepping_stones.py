# 문제를 풀 당시 생각 과정을 기입
'''
1칸 이동 : 작은 점프 n-1
2칸 이동 : 큰 점프
3칸 이동 : 매우 큰 점프 ,k 에너지

돌이 5개고 k는 4의 에너지일때
이때 가장 적은 에너지는 5가 된다.
첫판 0에서 1칸 뛰어서 0 1에서 2칸 이동해서 1 3에서 3칸 이동해서 도착 k=4
1+4 =5
이를 점화식으로 구현하면
dp[i] = min(dp[i-2] +dp[i-1] + k)
'''

# 풀이 코드 기입
n = int(input())
stones = [tuple(map(int, input().split())) for _ in range(n-1)]
k = int(input())



# 피드백 후 정리(알게된 점, 포인트 등)
'''

'''