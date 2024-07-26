# 문제를 풀 당시 생각 과정을 기입
'''
조합이란 n개 객체중 r개 객체를 선택하는 순서를 고려하지 않는 경우의 수로

n!/(n-m)!m! 라는 식으로 변환된다.
'''

# 풀이 코드 기입
n = int(input())
m = int(input())

x = 0
y = 0
z= 0
for i in range(1,n+1):
    x *= i
for i in range(1, n-m+1):
    y *= i
for i in range(1, m+1):
    z *= i

print(x//(y*z))


# 정답 코드 기입
# 팩토리얼 계산 함수 정의
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

n, m = list(map(int, input().split()))

# 팩토리얼을 사용하여 조합 계산
result = factorial(n) // (factorial(n - m) * factorial(m))

print(result)


# 피드백 후 정리(알게된 점, 포인트 등)
'''
comb라는 라이브러리를 사용하면 손쉽게 조합을 구현 가능

입력값을 list(map(int, input().split()))식으로 해서 한번에 입력받아 2개의 변수에 기입해야 함
'''