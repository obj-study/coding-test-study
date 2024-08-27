# 문제를 풀 당시 생각 과정을 기입
'''
- 접근 근거가 무엇인지 적어보기
문제가 길고 어려워보이지만, 차근차근 "순서대로" 구현하면 된다고 생각했다.
조금 길고 복잡할 뿐이지 문제될 부분은 하나도 없기 때문이다.

- 나의 접근에 문제점이 무엇일까 생각해보기
문제를 잘못 이해했다.
"3일 연속 전일대비 상승/하락" 을 "3일 연속 상승/하락"으로 받아들였다.
전자의 경우는 일수로 치면 4일 상승/하락이고 후자는 말그대로 3일 상승/하락이라 조건문의 구현이 달라진다.
단어 하나하나를 무시하지 않는 습관이 필요할 것 같다.

- 시간 복잡도를 고려해보기

'''

# 풀이 코드 기입
cash = int(input())

jh = cash
sm = cash

jh_cnt = 0
sm_cnt = 0

chart = list(map(int, input().split()))

for i, value in enumerate(chart):
    # jh
    if jh >= value:
        jh_cnt += jh // value
        jh = jh % value

    # sm
    if i >= 3:
        if chart[i-3] < chart[i-2] and chart[i-2] < chart[i-1] and chart[i-1] < value:
            sm += sm_cnt * value
            sm_cnt = 0
        if chart[i-3] > chart[i-2] and chart[i-2] > chart[i-1] and chart[i-1] > value:
            if sm >= value:
                sm_cnt += sm // value
                sm = sm % value

jh_money = jh + jh_cnt * chart[-1]
sm_money = sm + sm_cnt * chart[-1]


if jh_money > sm_money:
    print("BNP")
if sm_money > jh_money:
    print("TIMING")
if sm_money == jh_money:
    print("SAMESAME")

