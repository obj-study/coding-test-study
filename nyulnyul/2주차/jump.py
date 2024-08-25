# 문제를 풀 당시 생각 과정을 기입
'''
nxn을 이루는 행렬에 2중 배열을 통해 게임판을 먼저 구현한다.
게임의 규칙으로 반드시 오른쪽이나 아래로 이동 가능하며 현재 칸 위치만큼 이동해야 한다.
한 방향 점프는 무조건 한번만 가능하다
'''

# 풀이 코드 기입
n = int(input())
array = [[0] * n for _ in range(n)]
for i in range(n):
    A = list(map(int, input().split()))
    for j in range(n):
        array[i][j] =A[j]

# 행렬 출력
for i in range(n):
    for j in range(n):
        print(array[i][j], end=' ')
    print()

# 피드백 후 정리(알게된 점, 포인트 등)
'''
현재 위치 (i, j)에서 이동할 수 있는 칸 수를 move라고 할 때:
i + move가 게임판 내에 있다면 dp[i + move][j] += dp[i][j]
j + move가 게임판 내에 있다면 dp[i][j + move] += dp[i][j]
'''