# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
최대, 최소를 구한다. max, min 함수를 떠올렸고 사용 가능했다.

- 나의 접근에 문제점이 무엇일까 생각해보기

- 시간 복잡도를 고려해보기
1,000,000개의 수가 주어질 수 있고, 테스트 케이스는 최대 10개 까지이다.
그러면 최대 10,000,000개이므로 O(n)으로 짜면 된다.
min, max 함수는 o(n)이므로 풀이 가능했다.

'''

# 풀이 코드 기입
T = int(input())

for _ in range(T):
    n = int(input())
    li = list(map(int, input().split()))
    minimum = min(li)
    maximum = max(li)
    print(minimum, maximum)

