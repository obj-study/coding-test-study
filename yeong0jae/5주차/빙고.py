# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
사회자가 번호를 부를 때마다 빙고를 체크하면 된다고 생각했다. 빙고 체크는 시간복잡도가 n^2이지만
빙고판이 n=5로 작기떄문에 완전 탐색이 가능하다고 생각했다.

- 나의 접근에 문제점이 무엇일까 생각해보기ㄴ

- 시간 복잡도를 고려해보기
빙고판이 25로 고정되어있어서 고정된 시간복잡도가 구해진다. O(25*25). 25개에 대해서(빙고판 돌면서) 25개를 탐색(빙고 체크)

'''

# 풀이 코드 기입
bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))  # 빙고판 초기화

referee = []
for _ in range(5):
    for a in list(map(int, input().split())):  # 사회자 초기화
        referee.append(a)

def is_bingo(bingo):
    bingo_count = 0

    # 가로 빙고 체크
    for i in range(5):
        row_bingo = True
        for j in range(5):
            if bingo[i][j] != "*":
                row_bingo = False
                break
        if row_bingo: # 가로 빙고면 cnt +1
            bingo_count += 1

    # 세로 빙고 체크
    for j in range(5):
        col_bingo = True
        for i in range(5):
            if bingo[i][j] != "*":
                col_bingo = False
                break
        if col_bingo: # 세로 빙고면 cnt +1
            bingo_count += 1

    # 대각선 빙고 체크 (왼쪽 위 -> 오른쪽 아래)
    diagonal1_bingo = True
    for i in range(5):
        if bingo[i][i] != "*":
            diagonal1_bingo = False
            break
    if diagonal1_bingo: 
        bingo_count += 1

    # 대각선 빙고 체크 (오른쪽 위 -> 왼쪽 아래)
    diagonal2_bingo = True
    for i in range(5):
        if bingo[i][4-i] != "*":
            diagonal2_bingo = False
            break
    if diagonal2_bingo:
        bingo_count += 1

    return bingo_count

result = 0
flag = 0
for idx, a in enumerate(referee):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == a: # 사회자가 부른 값이면
                bingo[i][j] = "*" # *로 바꾸고
                result = is_bingo(bingo) # 빙고 확인
                if result >= 3: # 빙고 3개 이상되면 탈출
                    print(idx + 1)
                    flag = 1
                    break
        if flag == 1:
            break
    if flag == 1:
        break
