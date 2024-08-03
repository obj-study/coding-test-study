# 문제를 풀 당시 생각 과정을 기입
'''
길이 N인 수열 S
S[N]

S[i] 원하는 수를 골라 최대 K번 삭제

입력값 N 과 K
수열 수

수열에서 짝수로 이뤄진 연속 부분 수열중 가장 긴 길이
이를 위해 모두 짝수로 이뤄지도록 k개의 홀수를 삭제한다.

1~8중 최대 2개의 원소를 삭제해서 짝수로 이뤄지는 최대 수열 길이
ex)3과 5 제거 = 1, 2,4,6, 7 ,8 => 3

1은 제외하고 그 이후부터 k개의 홀수를 수열에서 제거 하는 구조
dp 타뷸레이션을 통해 반복문을 사용하여 하위 문제 해결 후 결과를 배열에 저장

n,k = map(int,input().split())
s = list(map(int,input().split()))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(0,k):
        if i>1 :
            if s[i] % 2 ==0 :
                dp[i][j] = dp[i-1][j] + 1
            else :
                dp[i][j] = dp[i - 1][j-1]
print(max(dp))
'''

# 풀이 코드 기입
n,k = map(int,input().split())
s = list(map(int,input().split()))

start, end, lens, max_len, del_cnt = 0,0,0,0,0

while end < len(s):
    if s[end] % 2 ==0:
        lens += 1
    else:
        del_cnt +=1
    while del_cnt > k:
        if s[start] % 2 != 0:
            del_cnt -= 1
        else:
            lens -=1
        start +=1
    max_len = max(max_len, lens)
    end+=1

print(max_len)





# 피드백 후 정리(알게된 점, 포인트 등)
'''
이 문제는 찾아본 결과 dp보단 슬라이딩 윈도우 or 투포인터 기법을 이용한다고 한다.
슬라이딩 윈도우랑 리스트에서 고정된 크기의 부분배열을 반복 사용시 효율적인 알고리즘으로 연속적 데이터 처리에 사용된다.

배열에서 부분배열(윈도우)의 크기를 정의하고 윈도우가 이동 할 때마다 새 요소와 제외된 요소를 고려해 업데이트 한다.
최대 크기나 특정 조건 만족까지 윈도우를 확장하거나 축소가능하다.


'''