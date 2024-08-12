# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
명령어마다의 동작이 있다 -> 함수로 만들어야겠다고 생각했다

- 나의 접근에 문제점이 무엇일까 생각해보기

- 시간 복잡도를 고려해보기
n, m 은 <4000이고 o(n)으로 충분히 풀린다

'''

# 풀이 코드 기입
n, m = map(int, input().split())
li = list(map(int, input().split()))

def first(li, i, x):
    li[i-1] = x

def second(li, l, r):
    for i in range(l-1, r):
        if li[i] == 0:
            li[i] = 1
        else:
            li[i] = 0

def third(li, l, r):
    for i in range(l-1, r):
        li[i] = 0

def fourth(li, l, r):
    for i in range(l-1, r):
        li[i] = 1

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        first(li, b, c)
    elif a == 2:
        second(li, b, c)
    elif a == 3:
        third(li, b, c)
    else:
        fourth(li, b, c)

print(" ".join(map(str, li)))

