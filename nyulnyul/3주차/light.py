# 문제를 풀 당시 생각 과정을 기입
'''
N개의 전구 맨왼쪽이 첫번째 -> 리스트
1 전구 켜짐 0 전구 꺼짐

1번 명령어 조건 1<=i<=n , x가 0or1 이면 i번째 전구 x로 변경
2번 명령어 조건 1<=l<=r<=n, l부터 r까지 전구 상태 변경
3번 명령어 조건 1<=l<=r<=n, l부터 r까지 전구 끔
4번 명령어 조건 1<=l<=r<=n, l부터 r까지 전구 킴


'''

# 풀이 코드 기입
N,M =map(int,input().split())# 전구개수 , 명령어 개수
lights = list(map(int, input().split())) # N개 전구 현재 상태 설정
for _ in range(M):
    a,l,r = map(int,input().split())
    l -= 1
    if a == 1:
        lights[l] = r
    elif a == 2:
        for i in range(l,r+1):
            if lights[i]==1 : lights[i]=0
            else : lights[i]=1
    elif a == 3:
        for i in range(l, r+1):
            lights[i] = 0
    else :
        for i in range(l, r + 1):
            lights[i] = 1

print(*lights)
# M+2줄까지 세개 정수 a(몇번째 명령어),b(i or l),c(x or r), 입력

# 피드백 후 정리(알게된 점, 포인트 등)
'''
print()에 변수명 앞에 *를 달면 공백을 구분하여 출력된다.
l이 무조건 r보다 작아야되기에 인덱스를 0부터 시작하도록 만들어 줘야 한다.

'''