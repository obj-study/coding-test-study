# 문제를 풀 당시 생각 과정을 기입
'''
예제에서 입력이 1이면 별이 *
입력이 2면
***** 5*5에 가운데에 직전 별
*   *
* * *
*   *
*****
입력이 3이면 9*9 가운데 기존꺼
*********
*       *
* ***** *
* *   * *
* * * * *
* *   * *
* ***** *
*       *
*********
입력이 4면
************* 13*13 가운데 기존꺼
*           *
* ********* *
* *       * *
* * ***** * *
* * *   * * *
* * * * * * *
* * *   * * *
* * ***** * *
* *       * *
* ********* *
*           *
*************

규칙 => 1 -> 5*5 -> 9*9 -> 13*13 = 4씩 증가 or n+(3*n-1)
'''

# 풀이 코드 기입
n = int(input())

arr=[n+(3*n-1)][n+(3*n-1)]

for i in range(arr):
    for j in range(arr):
        arr[i][j] += "*"

print(arr[i][j])

# 피드백 후 정리(알게된 점, 포인트 등)
'''
재귀를 할 줄 알아야 풀 수 있던 문제

'''