# https://www.acmicpc.net/problem/22857

# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
n개 길이(50000) 의 수열을 주어진 k(100) 수 만큼 다 지워보며 길이를 구한다? 최대 50000C100 -> 무조건 시간초과
완전탐색을 하되, 시간초과를 해결할 수 있는 방법을 생각해야했다.
부분 수열 탐색: 모든 가능한 부분 수열을 탐색하여 최대 길이를 찾는 것은 비효율적
수열을 한 번만 순회하면서 구간 내의 홀수 개수를 조절하면서 가장 긴 짝수 부분 수열의 길이를 찾으면 된다.
최대최소 갱신해나가는 탐색.

- 나의 접근에 문제점이 무엇일까 생각해보기
부분 수열 탐색: 모든 가능한 부분 수열을 탐색하여 최대 길이를 찾는 것은 비효율적
수열을 한 번만 순회하면서 구간 내의 홀수 개수를 조절하면서 가장 긴 짝수 부분 수열의 길이를 찾으면 된다.

투포인터를 많이 접해보지 못한 경험부족인 것 같다.
잘 정리하고 비슷한 투포인터 문제들을 풀어볼 필요가 있다.

- 시간 복잡도를 고려해보기
부분 수열 개수로 접근하면 (일반적인 완전탐색): O(n^2) * 각 수열 검토, 홀수 계산 까지 
투 포인터 : O(n) 한 번 순회하면서 최적의 값 찾으므로

'''

# 풀이 코드 기입
import sys
input = sys.stdin.readline

# 입력 처리
n, k = map(int, input().split())
li = list(map(int, input().split()))

# 변수 초기화
odd_count = 0  # 현재 구간 내의 홀수 개수
left = 0  # 구간의 시작 인덱스
right = 0  # 구간의 끝 인덱스
current_length = 0  # 현재 구간의 길이
max_length = 0  # 가장 긴 짝수 부분 수열의 길이

# 투 포인터를 사용하여 구간을 조정
while right < n:
    # 오른쪽 끝을 확장하며 처리
    if li[right] % 2 == 1:
        odd_count += 1
    
    # 홀수 개수가 k를 초과하면 왼쪽 끝을 이동시켜 조정
    # k개까지는 다 지울 수 있기 때문에 k개 까지는 홀수 허용하고 그 후 부터 왼쪽 이동시키는 전략
    while odd_count > k:
        if li[left] % 2 == 1:
            odd_count -= 1
        left += 1
    
    # 현재 구간에서 짝수 부분 수열의 길이 계산
    current_length = right - left + 1
    max_length = max(max_length, current_length - odd_count)
    
    # 오른쪽 끝을 다음으로 이동
    right += 1

print(max_length)  # 가장 긴 짝수 부분 수열의 길이 출력

