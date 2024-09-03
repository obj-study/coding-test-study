# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
입력 값에 따라 일졍 규칙의 별이 출력됨을 보고 규칙을 유추해야한다.
가로x세로만 기준으로 확인해보자
1 -> 1*1
2 -> 5*5 : +4 3
3 -> 9*9 : +4 6
4 -> 13*13 : +4 9
5 -> 17*17 : +4 12
값은 4만큼 증가하고 3의 배수로 증가함을 알 수 있었다.
숫자가 1 증가하면 행과 열의 길이가 4씩 증가를 확인 가능하다.
4 * n - 3의 규칙을 파악할 수 있다
단 여기서 문제는 예제에선 동일 길이의 행과 열 속에 이전 행과 열이 같이 출력되어야 한다.

기존 값을 반복해서 재귀된다



- 나의 접근에 문제점이 무엇일까 생각해보기(틀렸으면 쓰기)
재귀함수를 구현하는 방법을 몰랐음

- 시간 복잡도를 고려해보기
n의 값이 100이하이기에 최대 O(n)이라고 판단

- 스터디를 통해 알게된 점(필수x)

'''

# 풀이 코드 기입
import sys

size = int(sys.stdin.readline())
rule = 4*size-3
data= [['']*(size) for _ in range(size)]


def c_start(n,x,y):
    last = 4*n-3
    if n==1:
        data[x][y] = "*"
        return
    else:
        for i in range(last):
            data[x][y+i]="*"
            data[y+i][x] = "*"
            data[x+last-1][y + i] = "*"
            data[x+i][y+last-1] = "*"



##############################################

def c_start(n, x, y):
    last = 4 * n - 3
    if n == 1:
        data[x][y] = "*"
        return
    else:
        for i in range(last):
            data[x][y + i] = "*"
            data[y + i][x] = "*"
            data[x + last - 1][y + i] = "*"
            data[x + i][y + last - 1] = "*"
        c_start(n - 1, x + 2, y + 2)



size = int(input())
rule = 4 * size - 3
data = [[''] * (size) for _ in range(size)]

c_start(size, 0, 0)
for r in data:
    print(''.join(r))

##########################################
def draw_star(n):
    length = 4 * n - 3
    map_array = [[' '] * length for _ in range(length)]

    for i in range(n):
        start = 2 * i
        end = length - 1 - start

        for j in range(start, end + 1):
            map_array[start][j] = '*'
            map_array[end][j] = '*'
            map_array[j][start] = '*'
            map_array[j][end] = '*'

    return map_array


# 입력과 초기화
star = int(input())  # 별 개수
map_array = draw_star(star)

# 출력
for row in map_array:
    print(''.join(row))
