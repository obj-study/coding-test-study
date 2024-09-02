# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기

- 나의 접근에 문제점이 무엇일까 생각해보기
특정 키를 넣으면 위치를 출력하는 함수를 구현하는게 어려웠다.
일반적인 방향은 인덱스를 넣고 그 값을 출력하는 것인데, 이 문제는 값을 넣으면 인덱스를 뽑아야해서 생소했다.
해결 방법은 
1. 인덱스를 뽑는 enumerate를 활용하며 순회하는 것
2. 그리고 index()함수를 이용해 인덱스를 뽑는것이다

- 시간 복잡도를 고려해보기
findkey는 키보드의 키 갯수가 고정되어있으므로 O(1)이라고 볼 수 있고
findkey를 n번 반복하므로 O(n)이다.

'''

# 풀이 코드 기입

keyboard = [
    ['q','w','e','r','t','y','u','i','o','p'],
    ['a','s','d','f','g','h','j','k','l'],
    ['z','x','c','v','b','n','m']
]

lf, rf = input().split()
target = input()
target_len = len(target)

def find_key(keyboard, key):
    for row_index, row in enumerate(keyboard):
        if key in row:
            col_index = row.index(key)
            return (row_index, col_index)

lx, ly = find_key(keyboard, lf)
rx, ry = find_key(keyboard, rf)

time = 0
for k in target:
    a, b = find_key(keyboard, k)
    if (a <= 1 and b <= 4) or (a == 2 and b <= 3):
        time += abs(lx-a) + abs(ly-b)
        lx = a
        ly = b
    else:
        time += abs(rx-a) + abs(ry-b)
        rx = a
        ry = b
    time += 1
    
print(time)

