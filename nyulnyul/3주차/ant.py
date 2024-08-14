# 문제를 풀 당시 생각 과정을 기입
'''
준현은 BNP : 주식 안팖, 최대한 많이 살수 있는 만큼 즉시 매수
성민 : 전량 매수 전량 매도, 3일연속 상승한 주식 전량 매도, 3일연속 하락 주식 전량 매수

3일 연속의 주식 값을 비교

현금을 주가로 나눈 후 몫 => 주식 보유량 나머지 => 잔돈
'''

# 풀이 코드 기입
cash = int(input())
MachineDuck = list(map(int,input().split()))

jun = cash
juns = 0

for j in MachineDuck:
    if jun >= j:
        juns += jun // j
        jun %= j

jun_total = jun + juns * MachineDuck[-1]


sung = cash
sungs = 0

for i in range(3, len(MachineDuck)):
    # 3일 연속 하락
    if MachineDuck[i-3] > MachineDuck[i-2] > MachineDuck[i-1] > MachineDuck[i]:
        sungs += sung // MachineDuck[i]
        sung %= MachineDuck[i]
    # 3일 연속 상승
    elif MachineDuck[i-3] < MachineDuck[i-2] < MachineDuck[i-1] < MachineDuck[i]:
        sung += sungs * MachineDuck[i]
        sungs = 0


sung_total = sung + sungs * MachineDuck[-1]
if jun_total > sung_total:
    print("BNP")
elif jun_total < sung_total:
    print("TIMING")
else:
    print("SAMESAME")

# 피드백 후 정리(알게된 점, 포인트 등)
'''
성민이 if 할때 3개가 아닌 4개까지 봐야함
'''