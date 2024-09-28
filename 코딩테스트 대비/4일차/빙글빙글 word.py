'''
## 문제

동일한 길이의 `s`와 `t` 2개의 문자열이 주어집니다.

문자열 `s`를 변형하여 `t`와 동일해질 수 있는지 확인하려 합니다.

`s`를 변형하는 방식은 아래와 같습니다.

- `s`를 구성하는 문자를 한칸씩 오른쪽으로 이동합니다.
- 마지막 문자는 첫번째 자리로 이동합니다.
- 이 변형은 여러번 반복할 수 있습니다.

예를 들어 `s = "abcde"`라면, `s`를 변형해서 얻을 수 있는 문자열은

`"abcde"`, `"eabcd"`, `"deabc"`, `"cdeab"`, `"bcdea"`

로 총 5가지가 가능하다.

주어진 문자열 `s`, `t`에 대해서 `s`를 변형하여 `t`와 동일 문자열을 생성할 수 있는지 출력하시오.

## 입력설명

- `0 < s.length <= 10000`
- `0 < t.length <= 10000`

## 출력설명

문자열 `s`를 변형하여 `t`로 만들 수 있는지 논리형으로 반환

## 매개변수 형식

`s = "abcdef"`

`t = "efabcd"`

## 반환값 형식

`true`

[*** 풀이 (Python) (100/100) ***]
'''

def solution(s, t):
    case = []
    new_word = ''

    for i in range(len(s)):
        new_word = s[i:] + s[:i]
        case.append(new_word)
        i +=1

    for i in range(len(case)):
        if case[i] == t:
            answer = bool(1)
            break
        else:
            answer = bool(0)
    return answer

'''
모범답안

def solution(s, t):
    for i in range(len(s)):
        is_possible = True
        for j in range(len(s)):
            if s[(i+j)%len(s)] != t[j]:
                is_possible = False
        if is_possible:
            return True
    return False
            
'''