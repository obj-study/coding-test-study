# 문제를 풀 당시 생각 과정을 기입
'''
먼저 수열 크기 값과 수열 안을 이루는 내용물들을 넣고
dp를 통해 for문으로 계산
'''

# 풀이 코드 기입

n = int(input())
A = list(map(int, input().split()))


def largest_increasing_subsequence_sum(A):
    n = len(A)
    dp = [0] * n  # DP 배열 초기화

    for i in range(n):
        dp[i] = A[i]  # 초기값은 자기 자신
        for j in range(i):
            if A[j] < A[i]:  # 증가하는 부분 수열
                dp[i] = max(dp[i], dp[j] + A[i])

    return max(dp)  # 가장 큰 값 반환


print(largest_increasing_subsequence_sum(A))

# 예제 입력

# 피드백 후 정리(알게된 점, 포인트 등)
'''
이 문제는 dp를 이용해 풀어본다.
먼저 dp 배열을 초기화 하고 for문을 통해 계산하는데 이때 초기값을 A[i]로 각각 두고 한번 더 for문을 돈다
이때 A[2] < A[1] : 100 < 1 이면 아무것도 하지 않고 A[3] < A[2]이면 : 2 < 100 이기 때문에
기존 dp[2]인 100과 dp[3] + dp[2]인 102 둘중 최대값인 102로 dp[2]가 치환된다.
이를 계손 반복하여 dp 배열중 가장 큰 합을 출력한다.

설명을 보면 이해는 가는데 이거를 내 머리로 생각이 안...나
'''