# 문제를 풀 당시 생각 과정을 기입
'''
수열중 가장 긴 증가하는 부분 수열을 구하기
A = {10,20,10,30,20,50}중 10,20,30,50 부분만 직전에 비해 증가하는 값이기에 길이는 4
이 길이를 출력하기

n = int(input())
A = [0]
len = 0
for i in range(0,n):
    ni = int(input())
    A.append(ni)
    if ni> A[i-1] :
        len +=1
print(len)
'''

# 풀이 코드 기입

n = int(input())
A = list(map(int,input().split()))

dp = [1] * n # i가 0일때 증가 최대 부분 수열 길이는 1이기에 우선 1로 초기화
for i in range(1,n): # 1~n-1 인덱스까지의 모든 i
    for j in range(i): # i보다 작은 값 j
        if A[j] < A[i]: # j 원소가 i보다 작다 = 부분적 증가
            dp[i] = max(dp[i],dp[j] + 1) # i 에서의 최대 값 갱신


print(max(dp))

# 피드백 후 정리(알게된 점, 포인트 등)
'''
기존 코드대로 하니 런타임 에러가 났다.
그것은 두번째 입력때 for문으로 한번씩 받는게 아닌 한번에 값을 받기 때문이다.

A = list(map(int,input().split()))을 이용하면 한번에 입력받으며 list화 시킬 수 있다.

다이나믹 프로그래밍 원리로 이미 계산한 문제는 다시 계산할 수 없도록 해줘야 하며 
i에 대해 j를 일일이 확인하며 dp[i]를 업데이트 하는 문제이다.

이 문제의 점화식은 dp[i] = max(dp[i],dp[j]+1) 이다.

점화식 구성을 잘 해야 할 듯하다.
'''