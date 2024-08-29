# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
8*8 격자 위 10개의 지뢰
지뢰가 없는 지점 건드리면 주변 8개의 칸에 지뢰가 몇개인지 알리는 숫자
일부가 플레이 된 게임의 정보를 읽어 해당 격자를 출력

10>= n 입력
지뢰의 위치를 입력
n개의 한줄
. 은 지뢰 x *은 지뢰 o
이미 열린 칸 x
먼저 숫자를 입력 받고 행으로 8 열로 8의 배열을 만든다

그리고 한번더 8x8을 입력 받는다

둘을 비교해 x의 위치일때 주변 지뢰의 개수를 찾는다

2차원 배열 [i][j] 가 누른 지점일때 각각 +1 -1로 조힙되어 주변을 탐색 가능
arr[i+1][j+1] or arr[i][j+1] or arr[i-1][j+1] or arr[i+1][j] or arr[i][j] or arr[i-1][j] or arr[i+1][j-1] or arr[i][j-1] or arr[i-1][j-1] == "*":

- 나의 접근에 문제점이 무엇일까 생각해보기(틀렸으면 쓰기)
1. 인덱스 i-1 or j-1이 범위 초과일 경우를 고려 못함
2. 방향 벡터를 사용해서 하면 더 간결
3 리스트 형태를 문자열 형태로 변경
4. 게임 오버를 고려 못함


- 시간 복잡도를 고려해보기
각 칸마다 최대 8개의 주변 칸을 확인 = 모든 칸 탐색 = 판 크기 n x m => O(n*m)
이라곤 하지만 최악의 경우가  O(n*m)인건 알겠고 어떻게 이걸 유추하는지는 아직 잘 모름

- 스터디를 통해 알게된 점(필수x)

'''

# 풀이 코드 기입
n = int(input())

n = 8
arr = []
arr2 =[]
for i in range(n):
    nonplay = input()
    arr.append(list(nonplay))

for _ in range(n):
    played = input()
    arr2.append(list(played))


for i in range(n):
    for j in range(n):
        if arr2[i][j] == "x":
            count = 0
            if arr[i + 1][j + 1] == "*" or arr[i][j + 1] == "*" or arr[i - 1][j + 1] == "*" or arr[i + 1][j] == "*" or \
                    arr[i][j] == "*" or arr[i - 1][j] == "*" or arr[i + 1][j - 1] == "*" or arr[i][j - 1] == "*" or \
                    arr[i - 1][j - 1] == "*":
                count+=1
                arr2[i][j] = f"{count}"
            else:
                arr2[i][j] = "0"

for played in arr2:
    print(played)


#####################
n = int(input())
arr = []
arr2 = []

for i in range(n):
    nonplay = input()
    arr.append(list(nonplay))

for _ in range(n):
    played = input()
    arr2.append(list(played))

# 방향 벡터 (8방향)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

game_over = False

for i in range(n):
    for j in range(n):
        if arr2[i][j] == "x":
            if arr[i][j] == "*":
                game_over = True
            else:
                count = 0
                for k in range(8):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == "*":
                        count += 1
                arr2[i][j] = str(count)

# 게임 오버일 경우 모든 지뢰를 표시
if game_over:
    for i in range(n):
        for j in range(n):
            if arr[i][j] == "*":
                arr2[i][j] = "*"

# 결과 출력
for row in arr2:
    print("".join(row))
