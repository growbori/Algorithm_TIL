'''
## 문제

수학 천재 상호는 재미있는 규칙의 숫자를 찾는 것을 좋아한다.

상호는 이번에는 소인수가 `2`, `3`, `5`만으로 이루어진 숫자를 찾으려 한다.

위 조건을 만족하는 `n`번째 자연수를 구하는 프로그램을 작성하시오.

## 입력설명

- `0 < n <= 1000`

## 매개변수 형식

`5`

## 반환값 형식

`5`

## 예시 입출력 설명

조건을 만족하는 첫 10개의 숫자를 나열하면 아래와 같다.

`1`, `2`, `3`, `4`, `5`, `6`, `8`, `9`, `10`, `12`

[*** 풀이 (Python) (100/100) ***]
'''

def solution(n):
    dp = [0] * (n)
    dp[0] = 1
    mul2, mul3, mul5 = 0, 0, 0
    for i in range(1, n):
        val2 = dp[mul2] * 2
        val3 = dp[mul3] * 3
        val5 = dp[mul5] * 5
        dp[i] = min(val2, val3, val5)
        if dp[i] == val2:
            mul2 += 1
        if dp[i] == val3:
            mul3 += 1
        if dp[i] == val5:
            mul5 += 1

    return dp[-1]


'''
모범답안과 답안이 같음
'''