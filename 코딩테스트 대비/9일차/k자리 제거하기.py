'''
## 문제

양의 정수가 담긴 문자열 `s`가 있다고 하자. 이 문자열에서 `k`개의 숫자를 제거해, 가장 작은 숫자를 만들고자 한다.

이렇게 만든 가장 작은 숫자를 담은 문자열을 출력하시오.

단, `k`개의 문자열을 제거한 결과는 앞에 불필요한 `0`이 포함될 수 있으며,

최종 출력에는 이 불필요한 `0`는 제거하여 출력하시오. (예시 입출력 참고)

## 입력 설명

- `0 < s.length <= 10000`
- `0 < k <= s.length`

## 출력 설명

가장 작은 숫자를 문자열로 반환

## 입력 예시

`s = "105990"`

`k = 1`

## 출력 예시

`"5990"`

## 입출력 설명

맨 앞의 `'1'`을 제거하면 `"05990"`이 된다. 불필요한 `'0'`를 제거한 최종 출력은 `"5990"`이다.

[*** 풀이 (Python) (60/100) ***]
'''
def solution(s, k):
    answer = ''
    min_num = s
    for i in range(len(s)):
        new = s[:i] + s[i+k:]
        if int(min_num) > int(new):
            min_num = int(new)

    return str(min_num)

'''
모범답안

def solution(s, k):
    if k >= len(s):
        return "0"

    if k == 0:
        return s.lstrip('0')
    
    if s[1] == '0':
        return solution(s[1:].lstrip('0'), k-1)
    else:
        ind = 0
        for i in range(1, len(s)):
            if s[i-1] < s[i]:
                ind = i
            elif s[i-1] != s[i]:
                break
        return solution(s[:ind] + s[ind+1:], k-1)

'''