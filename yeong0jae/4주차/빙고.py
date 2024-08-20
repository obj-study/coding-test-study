# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
사회자가 번호를 부를 때마다 빙고를 체크하면 된다고 생각했다. 빙고 체크는 시간복잡도가 n^2이지만
빙고판이 n=5로 작기떄문에 완전 탐색이 가능하다고 생각했다.

- 나의 접근에 문제점이 무엇일까 생각해보기

- 시간 복잡도를 고려해보기
빙고판이 25로 고정되어있어서 고정된 시간복잡도가 구해진다. O(25*25). 25개에 대해서(빙고판 돌면서) 25개를 탐색(빙고 체크)

'''

# 풀이 코드 기입
bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

referee = []
for _ in range(5):
    for a in list(map(int, input().split())):
        referee.append(a)

def is_bingo(bingo):
    bingo_count = 0
    
    # 가로 빙고 체크
    for i in range(5):
        if all(x == "*" for x in bingo[i]):
            bingo_count += 1
    
    # 세로 빙고 체크
    for j in range(5):
        if all(bingo[i][j] == "*" for i in range(5)):
            bingo_count += 1
    
    # 대각선 빙고 체크
    if all(bingo[i][i] == "*" for i in range(5)):
        bingo_count += 1
    if all(bingo[i][4-i] == "*" for i in range(5)):
        bingo_count += 1
    
    return bingo_count

result = 0
flag = 0
for idx, a in enumerate(referee):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == a:
                bingo[i][j] = "*"
                result = is_bingo(bingo)
                if result >= 3:
                    print(idx + 1)
                    flag = 1
                    break
        if flag == 1:
            break
    if flag == 1:
        break
