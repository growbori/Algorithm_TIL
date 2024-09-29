'''
## 문제

두 개의 문자열 `s`, `t`가 주어져 있다.

두 문자열이 정확히 '한끗차이'일 경우 `true`, 아닐 경우 `false`를 반환하시오.

한끗차이는 아래 셋 중 하나를 만족하면 된다.

- `s`에서 문자 하나를 삭제하여 `t`를 만들 수 있다.
- `s`에서 문자 하나를 추가하여 `t`를 만들 수 있다.
- `s`에서 문자 하나를 변경하여 `t`를 만들 수 있다.

## 입력설명

- `0 <= s.length() <= 100000`
- `0 <= t.length() <= 100000`

## 매개변수 형식

`s = "zEroBase"`

`t = "zeroBase"`

## 반환값 형식

`true`

## 예시 입출력 설명

두번째 문자 `E`를 `e`로 변경하면 되므로, 두 문자열은 한끗차이이다.

[*** 풀이 (Python) (100/100) ***]
'''

def solution(s, t):
    if s == t:
        return False
    
    if abs(len(s) - len(t)) > 1:
        return False

    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            if s[i+1:] == t[i+1:]:
                return True
            
            if s[i+1:] == t[i:]:
                return True
            
            if s[i:] == t[i+1:]:
                return True
            
            return False
    
    if abs(len(s) - len(t)) == 1:
        return True
    
    return False


'''
모범답안과 답안 동일함
'''