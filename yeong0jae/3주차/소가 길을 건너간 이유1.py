# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
특정 소가 위치를 바꾸는 것을 감지하고, 횟수를 기록해야했다.
그런데 소가 10마리밖에 없으므로, 소의 번호를 인덱스로 하는 크기 11짜리 리스트로 횟수를 더해나가면 된다.
횟수를 누적하는 리스트, 그리고 위치를 기억하는 리스트로 두개를 사용했다.

- 나의 접근에 문제점이 무엇일까 생각해보기

- 시간 복잡도를 고려해보기
주어진 관찰은 최대 100번, 소는 10마리이다.
수도 엄청 적은데 알고리즘도 그냥 선형 탐색이라 O(N)이다

'''

# 풀이 코드 기입
n = int(input())

cnt = [0] * 11
position = [-1] * 11

for _ in range(n):
    num, pos = map(int, input().split())
    if not position[num] == -1:
        if position[num] != pos:
            cnt[num] += 1
            position[num] = pos
    else:
        position[num] = pos

print(sum(cnt))

