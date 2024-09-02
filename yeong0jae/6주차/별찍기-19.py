# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
n에 따라 모양은 결정되어있다. 그리고 규칙이 있으므로 n에 대한 일반화된 값들을 찾고, 그 값을 가지고
사각형을 그리면 된다고 생각했다. 처음부터 완벽하게 코드가 그려지지 않아도
n번 그림이 반복되니까 일단 for i in range(n)을 먼저 하고,
좌표를 지정하고, 사각형을 그리고..
구현 문제의 특징은 하나하나 차근차근 짜는 거라는 걸 다시금 느끼게 해준 문제다

- 나의 접근에 문제점이 무엇일까 생각해보기


- 시간 복잡도를 고려해보기
이차원 배열을 돌으므로 O((size)^2)이다. 간단히는 O(n^2). n은 100이므로 문제 없음

'''

# 풀이 코드 기입

n = int(input())
size = 4 * n - 3 # 일반화된 n에 따른 사이즈
matrix = [[' ' for _ in range(size)] for _ in range(size)] # size에 따른 빈 좌표

for i in range(n): # n번 반복
    start = 2 * i
    end = size - 2 * i - 1 # 사각형 시작, 끝 좌표
    for j in range(start, end + 1): # 사각형 그리기
        matrix[start][j] = '*'
        matrix[end][j] = '*'
        matrix[j][start] = '*'
        matrix[j][end] = '*'

for line in matrix:
    print(''.join(line))
