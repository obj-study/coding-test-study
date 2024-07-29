# 문제를 풀 당시 생각 과정을 기입
'''
조합 계산을 해서 구해야겠다고 생각했다
'''

# 풀이 코드 기입
n, m = map(int, input().split())

numerator = 1
denumerator = 1

for i in range(n, n-m, -1):
    numerator *= i

for i in range(1, m+1):
    denumerator *= i

print(numerator // denumerator)

