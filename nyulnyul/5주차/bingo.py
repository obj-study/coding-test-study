# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
가로와 세로는 각각 5개
빙고가 되는 기준 가로,세로,왼쪽위에서 오른쪽 아래 대각선,오른쪽 위에서 왼쪽 아래 대각선
- 나의 접근에 문제점이 무엇일까 생각해보기(틀렸으면 쓰기)

- 시간 복잡도를 고려해보기

- 스터디를 통해 알게된 점(필수x)

'''

# 풀이 코드 기입
def check_bingo(board):
    count = 0

    # 가로 줄 확인
    for i in range(5):
        if sum(board[i]) == 0:
            count += 1

    # 세로 줄 확인
    for i in range(5):
        if sum([board[j][i] for j in range(5)]) == 0:
            count += 1

    # 대각선 확인 (왼쪽 위에서 오른쪽 아래)
    if sum([board[i][i] for i in range(5)]) == 0:
        count += 1

    # 대각선 확인 (오른쪽 위에서 왼쪽 아래)
    if sum([board[i][4-i] for i in range(5)]) == 0:
        count += 1

    return count

# 입력 받기
bingo_board = [list(map(int, input().split())) for _ in range(5)]
called_numbers = [list(map(int, input().split())) for _ in range(5)]

# 숫자를 부를 때마다 확인
called_count = 0
for i in range(5):
    for j in range(5):
        called_count += 1
        number = called_numbers[i][j]

        # 부른 숫자를 빙고판에서 0으로 표시
        for x in range(5):
            for y in range(5):
                if bingo_board[x][y] == number:
                    bingo_board[x][y] = 0

        # 빙고 개수 확인
        if check_bingo(bingo_board) >= 3:
            print(called_count)
            exit()