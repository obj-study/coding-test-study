# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
3주차의 전구 문제처럼 겉보기엔 복잡해보이지만 문제를 쭉 읽고나면 그냥 구현하면 되는 문제란 걸 알수있다
스위치도 100개 이하고, 학생수도 100개 이하이므로 시간복잡도도 널널하다

- 나의 접근에 문제점이 무엇일까 생각해보기

- 시간 복잡도를 고려해보기
O(학생 수 * n)이다. 한 학생은 최대 o(n)짜리 선형탐색을 하기 때문
'''

# 풀이 코드 기입
n = int(input())

switch = list(map(int, input().split()))
stu_num = int(input())
students = []
for _ in range(stu_num):
    students.append(list(map(int, input().split())))

def switch1(li, x):
    if li[x] == 1:
        li[x] = 0
    else:
        li[x] = 1
def switch2(li, x):
    left_end = 0
    right_end = len(li) - 1
    i = 1
    switch1(li, x)
    while x-i >= left_end and x+i <= right_end:
        if li[x-i] == li[x+i]:
            switch1(li, x-i)
            switch1(li, x+i)
        else:
            break
        i += 1  

for gender, number in students:
    if gender == 1:
        while number <= n:
            switch1(switch, number-1)
            number *= 2
    if gender == 2:
        switch2(switch, number-1)

print(" ".join(map(str, switch)))
