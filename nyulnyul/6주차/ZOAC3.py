# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
각 키를 누르는데 1의 시간, 동시 양손 사용 불가 키보드는 쿼티식
손가락 이동시간 a좌표(x1,y1) b좌표(x2,y2)면 거리 |x1-x2| + |y1-y2|
문자열 출력 최소 시간 구하기

첫 입력 왼손,오른손 처음 위치
다음줄 길이 최대 100자의 문자열

출력 : 입력 문자열 출력의 최솟값

왼속영역과 오른손 영역 분리

- 나의 접근에 문제점이 무엇일까 생각해보기(틀렸으면 쓰기)
접근 방식은 나쁘지 않았지만 좌표로 변환 하는 과정에서 미숙했다고 봄
key_positions 딕셔너리를 통해 좌표를 저장하고 초기위치를 받아 저장후 순회하면서 판단해 업데이트
이 과정에서 total을 통한 누적값을 이용해 최소시간을 출력하는 문제였다.

- 시간 복잡도를 고려해보기
qwerty배열은 크기가 고정되어있어서 O(1)
입력 문자열의 길이 n이고 n개의 문자를 처리 할 때 순회 for문 하나 O(n)
따라서 빅오에 의해 O(n)

- 스터디를 통해 알게된 점(필수x)

'''
import sys
qwerty = [["q","w","e","r","t","y","u","i","o","p"],
          ["a","s","d","f","g","h","j","k","l"],
          ["z","x","c","v","b","n","m"]]

leftArea = ["q","w","e","r","t","a","s","d","f","g","z","x","c","v"]
# 손가락 위치
firstFinger = sys.stdin.readline()
leftFinger,rightFinger = firstFinger.split(" ")
print(leftFinger)
print(rightFinger)

#문자열 입력
inputString = sys.stdin.readline()

xVal = [0]*100
yVal = [0]*100

for i in range(3):
    for j in range(len(qwerty)):
        if leftFinger == qwerty[i][j]:
            xVal.append(i)
            yVal.append(j)

total =0
for i in range(inputString):
    if i in leftArea: #왼속손
        total +=  abs(xVal[i-1]-xVal[i])+abs(yVal[i-1]-yVal[i]) + 1
    else: #오른손
        total += abs(xVal[i - 1] - xVal[i]) + abs(yVal[i - 1] - yVal[i]) + 1
# 풀이 코드 기입
import sys
qwerty = [["q","w","e","r","t","y","u","i","o","p"],
          ["a","s","d","f","g","h","j","k","l"],
          ["z","x","c","v","b","n","m"]]

leftArea = ["q","w","e","r","t","a","s","d","f","g","z","x","c","v"]
# 손가락 위치
firstFinger = sys.stdin.readline()
leftFinger,rightFinger = firstFinger.split(" ")
print(leftFinger)
print(rightFinger)

#문자열 입력
inputString = sys.stdin.readline()

xVal = [0]*100
yVal = [0]*100

for i in range(3):
    for j in range(len(qwerty)):
        if leftFinger == qwerty[i][j]:
            xVal.append(i)
            yVal.append(j)

total =0
for i in range(inputString):
    if i in leftArea: #왼속손
        total +=  abs(xVal[i-1]-xVal[i])+abs(yVal[i-1]-yVal[i]) + 1
    else: #오른손
        total += abs(xVal[i - 1] - xVal[i]) + abs(yVal[i - 1] - yVal[i]) + 1

######################################################################
import sys
qwerty = [["q","w","e","r","t","y","u","i","o","p"],
          ["a","s","d","f","g","h","j","k","l"],
          ["z","x","c","v","b","n","m"]]

leftArea = ["q","w","e","r","t","a","s","d","f","g","z","x","c","v"]
# 손가락 위치
firstFinger = sys.stdin.readline()
leftFinger,rightFinger = firstFinger.split(" ")
print(leftFinger)
print(rightFinger)

#문자열 입력
inputString = sys.stdin.readline()

# 각 문자의 위치를 찾기 위한 좌표 사전 생성
key_positions = {}
for i in range(3):
    for j in range(len(qwerty[i])):
        key_positions[qwerty[i][j]] = (i, j)

# 첫 손가락 위치를 좌표로 변환
lx, ly = key_positions[leftFinger]
rx, ry = key_positions[rightFinger]

total =0
for char in inputString:
    cx, cy = key_positions[char]
    if char in "qwertasdfgzxcv":  # 왼손 사용 영역
        total += abs(lx - cx) + abs(ly - cy) + 1
        lx, ly = cx, cy
    else:  # 오른손 사용 영역
        total += abs(rx - cx) + abs(ry - cy) + 1
        rx, ry = cx, cy

print(total)