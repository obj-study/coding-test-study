
## ✏️ 스터디 방식

7.22(월) ~ `매주 월요일` 진행

언어 : Python or JAVA 각자 선택

- 백준 선별 문제

https://github.com/tony9402/baekjoon

## 📚 스터디 진행 순서

1. 풀 문제는 위의 백준 선별 문제에서 `주 5~7문제` 씩 선정
2. 선정한 문제들을 `각자 풀어오기`
3. 공유한 깃허브 저장소에 각자 풀이를 `commit & push`
4. 스터디 시간에 서로의 `생각 과정과 풀이 접근 방법을 공유`

## 📝 문제 풀이 순서

1. 문제를 풀 당시의 `생각 과정`을 기입 - (짧게 기입해도 됩니다. 본인의 문제 풀 당시 생각 과정을 적기)
2. `풀이 코드` 작성
3. 피드백 후 정리 - (`알게된 점`, `풀이 포인트` 등을 정리해서 기입)
    - 예시 템플릿
        
        ```python
        **# 문제를 풀 당시 생각 과정을 기입**
        '''
        
        '''
        
        **# 풀이 코드 기입**
        
        **# 피드백 후 정리(알게된 점, 포인트 등)**
        '''
        
        '''
        ```
        
    - Boj 2839번 문제 풀이 예시 - https://www.acmicpc.net/problem/2839
        
        ```python
        **# 문제를 풀 당시의 생각 과정을 기입**
        '''
        만약 18kg의 무게를 구성하는 최소 개수를 구한다고 하면, 이는 18kg이전 무게값으로 구해질 수 있는 여지가 있다.
        문제 상황이 이전 상황과 엮여서 완전탐색이 안되고, 이전 결과값을 재사용해야 한다.
        그래서 점화식이 작성되고, dp로 풀 수 있다
        i와 di를 정의한 후
        d[i]가 조합되는 여러 경우 중 최소값을 구하기. -> d[i] = min(d[i-3] + 1, d[i-5] + 1) min을 활용한 점화식
        '''
        
        **# 풀이 코드 기입**
        n = int(input())
        
        inf = 1e9
        
        d = [inf] * (5001)
        
        d[3] = 1
        d[5] = 1
        
        for i in range(7, 5001):
            d[i] = min(d[i-3] + 1, d[i-5] + 1)
        
        answer = d[n]
        if answer >= inf:
            print(-1)
        else:
        		print(answer)
        
        **# 피드백 후 정리(알게된 점, 포인트 등)**
        
        '''
        1. 최댓값으로 초기화 할 때 inf = 1e9를 쓸 수 있다. 10의 9승(10억)
        2. 문제가 완전탐색이 안되고, 이전 결과값을 활용할 수 있는 유형이다. i를 정의하고 d를 도출하는 점화식 세우기
        3. d[i] = min(d[i-3] + 1, d[i-5] + 1)와 같은 min, max 함수를 활용하는 유형
        '''
        ```
        
    - Boj 1620번 문제 풀이 예시 - https://www.acmicpc.net/problem/1620
        
        ```python
        # 생각 과정
        '''
        처음엔 index를 이용해서 풀어보려고 했지만, 시간복잡도가 O(n^2)이라서 시간초과가 날 것 같아서 다른 방법을 생각함 (for x index() = n^2)
        -> 인덱스와 value를 매핑한 딕셔너리를 이용해 O(1) * O(n)으로 해결할 수 있었다.
        -> 핵심 아이디어는 딕셔너리를 양방향으로 두개 만드는 것이다. key, value를 서로 바꿔서 저장한다.
        ++ 두개 만들 필요없이 하나의 딕셔너리에 양방향 데이터를 모두 넣어도 됨.. (key, value), (value, key) 둘 다 넣어두면 됨
        '''
        
        # 풀이 코드
        import sys
        def input(): return sys.stdin.readline().rstrip()
        
        n, m = map(int, input().split())
        
        poks = []
        for _ in range(n):
            poks.append(input())
        
        pdic1 = {}
        pdic2 = {}
        for idx, val in enumerate(poks):
            pdic1[idx+1] = val
            pdic2[val] = idx+1
        
        answer = []
        for _ in range(m):
            s = input()
            if s.isdigit():
                answer.append(pdic1[int(s)])
            else:
                answer.append(pdic2[s])
        
        for e in answer:
            print(e)
        
        # 피드백 후 정리
        '''
        1. 어떤 문자열이 정수로 이루어져 있는지 확인하는 방법은 isdigit()을 사용한다.
        2. 특정 값에 대한 인덱스가 묶여있는 경우 딕셔너리를 생각한다. 딕셔너리는 key에 따른 value값을 찾는데에 O(1)이므로 시간복잡도에서 유리하다.
        3. n이 100,000쯤 되는데 n^2의 시간복잡도가 나오면 map(in 연산자, 딕셔너리, hash함수 등) 을 의심해볼만하다.
        '''
        ```
