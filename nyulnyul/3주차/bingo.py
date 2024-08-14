# 문제를 풀 당시 생각 과정을 기입
'''
5x5로 이뤄진 판 => 2중배열
'''

# 풀이 코드 기입

bingo = [[0 for col in range(5)] for row in range(5)]
MCbingo = [[0 for col in range(5)] for row in range(5)]
score = 0

x = []
for i in range(5):
    for j in range(5):
        x = list(map(int,input().split()))
        bingo.append(x)

for i in range(5):
    for j in range(5):
        x = list(map(int,input().split()))
        MCbingo.append(x)
        if(bingo[i][j] == MCbingo[i][j]):
            score +=1

########################'
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

# 피드백 후 정리(알게된 점, 포인트 등)
'''
빙고 완성 여부 확인 후 빙고가 3개 완성되는 시점을 찾아야한다.
'''