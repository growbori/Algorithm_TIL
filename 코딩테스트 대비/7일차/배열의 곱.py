'''
## 문제

두 개의 배열이 RLE(running length encoding)으로 부호화 되어 있다.

RLE는 동일한 값이 연속으로 있을 때, 해당 값이 몇 번 반복되는지 표기하는 부호화 방식이다.

예를 들어 `{1, 1, 1, 1, 2, 2, 2, 5, 4}`라는 배열이 있을 때, 이 배열을 RLE로 부호화하는 과정은 아래와 같다.

- `1`이 `4`번 반복되므로 `{1, 4}`로 부호화
- `2`가 `3`번 반복되므로 `{2, 3}`로 부호화
- `5`가 `1`번 반복되므로 `{5, 1}`로 부호화
- `4`가 `1`번 반복되므로 `{4, 1}`로 부호화
- 위 부호를 순서대로 배치하여 최종 부호 `{{1, 4}, {2, 3}, {5, 1}, {4, 1}}`을 얻는다.

위와 같이 RLE로 부호화된 배열이 `s`와 `t` 두 개가 주어져 있다.

이 두 배열의 원본 배열을 `s_decoded`, `t_decoded`라 할 때, 두 배열의 각 요소를 곱한 값으로 구성된 `u_decoded` 배열을 RLE로 부호화한 결과를 출력하시오.

즉, `u_decoded[i] = s_decoded[i] * t_decoded[i]`이며, 최종 RLE 결과는 `u_decoded`를 가능한한 짧게 부호화한 결과여야 한다.

단, `s_decoded`와 `t_decoded`의 길이는 항상 같게 주어진다.

## 입력설명

- `0 < s.length <= 1000`
- `0 < t.length <= 1000`

## 출력설명

RLE로 부호화한 결과를 2차원 정수 배열로 반환

## 매개변수 형식

`s = {{1, 4}, {2, 2}}`

`t = {{6, 4}, {3, 2}}`

## 반환값 형식

`{{6, 6}}`

## 예시 입출력 설명

`s_decoded = {1, 1, 1, 1, 2, 2}`이고,

`t_decoded = {6, 6, 6, 6, 3, 3}`이므로,

`u_decoded = {6, 6, 6, 6, 6, 6}`이 된다.

이것을 RLE로 부호화 하면 `u = {{6, 6}}`이다.

[*** 풀이 (Python) (40/100) ***]
'''

def solution(s, t):
    s_decode = []
    t_decode = []

    for i in range(len(s)):
        for j in range(s[i][1]):
            s_decode.append(s[i][0])

    for i in range(len(t)):
        for j in range(t[i][1]):
            t_decode.append(t[i][0])

    u_decode = []
    for i in range(len(s_decode)):
        u_decode.append(s_decode[i] * t_decode[i])


    fin = []

    for i in range(len(u_decode)):
        x = u_decode.count(u_decode[i])
        if [u_decode[i], x] not in fin:
            fin.append([u_decode[i], x])
        else:
            continue
    return fin

'''
모범답안

def solution(s, t):
    idx1 = 0
    idx2 = 0
    res = []

    while idx1 < len(s) or idx2 < len(t):
        if idx1 < len(s) and idx2 < len(t):
            min_freq = min(s[idx1][1], t[idx2][1])
            mul = s[idx1][0] * t[idx2][0]
            if min_freq == s[idx1][1]:
                idx1 += 1
            else:
                s[idx1][1] -= min_freq
            if min_freq == t[idx2][1]:
                idx2 += 1
            else:
                t[idx2][1] -= min_freq
        elif idx1 < len(s):
            min_freq = s[idx1][1]
            mul = s[idx1][0]
            idx1 += 1
        else:
            min_freq = t[idx2][1]
            mul = t[idx2][0]
            idx2 += 1

        if len(res) > 0 and mul == res[-1][0]:
            res[-1][1] += min_freq
        else:
            res.append([mul, min_freq])
    return res

'''