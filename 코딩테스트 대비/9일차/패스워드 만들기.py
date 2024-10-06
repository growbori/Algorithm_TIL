'''
## 문제

당신은 제로쇼핑의 백엔드 서버 개발을 맡게 되었다.

이번에 배정받은 업무는 강력한 비밀번호 확인 기능으로, 사용자가 무작위 공격으로부터 안전하게 돕는 기능이다.

당신은 입력받은 문자열 `s`가 아래 조건을 만족하는지 확인해야 한다.

- 비밀번호는 6자 이상, 20자 이하로 이루어진다.
- 비밀번호는 최소 하나 이상의 영문자 소문자, 영문자 대문자, 숫자, 그리고 특수문자(`!@#$%^&*()`)로 이루어진다.
- 비밀번호는 똑같은 문자가 세 번 반복되지 않는다.
- 셋 이상 연속된 영문자 또는 숫자가 존재하지 않는다. 이 때, 영문자는 대소문자 구분을 하지 않는다. (ex. `abc`, `123`, `DeF`, `987`)

입력받은 문자열 `s`가 위 조건을 만족하는지 반환하는 프로그램을 작성하시오.

## 입력설명

- `0 < s.length <= 100`

## 매개변수 형식

`s = "zeRobAsE!2#4"`

## 반환값 형식

`true`


[*** 풀이 (Python) (100/100) ***]
'''

def solution(s):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha_A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sig = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    answer = True
    if len(s) < 6 or len(s) > 20:
        answer = False
    count_alpha = 0
    count_alpha_A = 0
    count_nums = 0
    count_sig = 0
    for i in range(len(s)):
        if s[i] in alpha:
            count_alpha += 1
        elif s[i] in alpha_A:
            count_alpha_A += 1
        elif s[i] in '0123456789':
            count_nums += 1
        elif s[i] in sig:
            count_sig += 1

    if count_alpha == 0 or count_alpha_A == 0 or count_nums == 0 or count_sig == 0:
        answer = False
    else:
        answer = True
    for j in range(len(s)-2):
        if s[j] == s[j+1] == s[j+2]:
            answer = False
    for j in range(len(s)-2):
        if s[j].isdigit() and s[j+1].isdigit() and s[j+2].isdigit():
            if int(s[j]) + 1 == int(s[j+1]) and int(s[j+1]) + 1 == int(s[j+2]):
                answer = False
    for j in range(len(s)-2):
        for i in range(len(alpha)-2):
            if (s[j] == alpha[i] or s[j] == alpha_A[i]) and (s[j+1] == alpha[i+1] or s[j+1] == alpha_A[i+1]) and (s[j+2] == alpha[i+2] or s[j+2] == alpha_A[i+2]):
                answer = False
                break

    return answer


'''
모범답안

from string import ascii_lowercase, ascii_uppercase


SPECIAL = '!@#$%^&*()'

def solution(s):
    if len(s) < 6 or len(s) > 20:
        return False
    
    lower = 0
    upper = 0
    digit = 0
    special = 0
    for c in s:
        if c in ascii_lowercase:
            lower += 1
        elif c in ascii_uppercase:
            upper += 1
        elif '0' <= c <= '9':
            digit += 1
        elif c in SPECIAL:
            special += 1
        
        if lower and upper and digit and special:
            break
    else:
        return False
    
    repeat = 0
    ascend = 0
    descend = 0
    
    for c1, c2 in zip(s.lower(), s[1:].lower()):
        if c1 == c2:
            repeat += 1
            ascend = 0
            descend = 0
        elif ord(c2) - ord(c1) == 1:
            ascend += 1
            descend = 0
            repeat = 0
        elif ord(c2) - ord(c1) == -1:
            descend += 1
            ascend = 0
            repeat = 0
        else:
            ascend = 0
            descend = 0
            repeat = 0

        if ascend == 2 or repeat == 2 or descend == 2:
            return False
    
    return True

# s = "zErOBase)12#Few545"
# print(solution(s))
'''