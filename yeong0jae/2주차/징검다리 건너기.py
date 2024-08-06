# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
완전탐색을 시도했을 때 바텀업으로 경우의수가 수없이 뻗어나간다
재사용 가능성을 보고 dp라고 판단했다.
max(1칸전 d값 + 한칸 소모값, 2칸전 d값 + 2칸 소모값)
으로 값을 깔아둔 후
깔아둔 dp 테이블 에다가 3칸 점프 dp를 돌리면 된다.

- 나의 접근에 문제점이 무엇일까 생각해보기

- 시간 복잡도를 고려해보기
3칸 점프를 고려할 때 이중반복문에 의해 O(n^2)이다.
주어진 n값은 최대20 이므로 통과된다
ㄴ
'''

# 풀이 코드 기입
n = int(input())
jump = [[0, 0]]
for _ in range(n-1):
    jump.append(map(int, input().split()))
k = int(input())

d = [0] * (n+1)

if n == 1:
    print(0)
if n == 2:
    print(jump[1][0])
else:
    d[1] = jump[1][0]
    d[2] = min(d[1] + jump[2][0], jump[1][1])

    for i in range(3, n):
        d[i] = min(d[i-1] + jump[i][0], d[i-2] + jump[i-1][1])
    
    answer = d[n-1]

    for i in range(3, n):
        d2 = d[:]
        d2[i] = d[i-3] + k

        for j in range(i+1, n):
            d2[j] = min(d2[j-1] + jump[j][0], d2[j-2] + jump[j-1][1])
        
        if answer > d2[n-1]:
            answer = d2[n-2]

    print(answer)
