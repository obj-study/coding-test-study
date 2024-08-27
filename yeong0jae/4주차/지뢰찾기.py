# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
격자가 나왔으니 완전탐색 시뮬레이션일 수 있고, 그래프 탐색 문제일 수도 있다고 생각했다.
문제를 읽어보니 방향 리스트를 정의하고 이차원 리스트를 탐색하면 된다고 생각했고 그렇게 풀렸다.

- 나의 접근에 문제점이 무엇일까 생각해보기

- 시간 복잡도를 고려해보기
n은 10이하이므로 이차원 완전 탐색이 충분히 가능하다

'''

# 풀이 코드 기입
n = int(input())

open_map = []
for _ in range(n):
    open_map.append(list(input()))
play_map = []
for _ in range(n):
    play_map.append(list(input()))

def count_bug(li, x, y):
    v_list = [[-1, 0], [-1, 1], [-1, -1], [0, -1], [0, 1], [1, 0], [1, -1], [1, 1]]
    bug_cnt = 0
    for v in v_list:
        search_x = x + v[0]
        search_y = y + v[1]
        if 0 <= search_x < n and 0 <= search_y < n:
            if li[search_x][search_y] == "*":
                bug_cnt += 1
    return bug_cnt

# 지뢰를 클릭한 경우를 추적하기 위한 플래그
mine_clicked = False

for i in range(n):
    for j in range(n):
        if play_map[i][j] == "x":
            if open_map[i][j] == "*":
                mine_clicked = True
            else:
                cnt = count_bug(open_map, i, j)
                play_map[i][j] = str(cnt)

# 지뢰를 클릭한 경우, 모든 지뢰를 표시
if mine_clicked:
    for i in range(n):
        for j in range(n):
            if open_map[i][j] == "*":
                play_map[i][j] = "*"

for line in play_map:
    print("".join(line))
