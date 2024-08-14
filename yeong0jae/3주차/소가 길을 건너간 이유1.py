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

- 스터디를 통해 알게된 점
다른 풀이 (딕셔너리를 이용한 풀이)로도 풀리고, 내 풀이로도 풀리는 이유는
근본적인 접근은 결국 같기 때문이다.
딕셔너리를 이용한 것은 소의 번호에 따른 위치값을 저장한 것인데 (Key, Value)
내 풀이는 "딕셔너리"라는 자료형만 이용하지 않았을 뿐이지 리스트 (크기 10짜리 position)를 통해 인덱스를 key로 사용하는 매핑을 구현한거다.
하지만 가독성과 코드적으로 딕셔너리가 더 의도에 맞고 목적에 맞다고 생각한다.

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

# 딕셔너리를 이용한 풀이
n = int(input())
last = {}
count = 0

for i in range(n):
    cow, pos = map(int, input().split())
    if cow in last:
        if last[cow] != pos:
            count += 1
    last[cow] = pos
print(count)