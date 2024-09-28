'''
## 문제

이번에 회원 관리 프로그램을 만들면서 고객에게 ID 와 '비밀번호'를 입력받아야 하는 기능을 개발해야 합니다.

그 중 '비밀번호' `s`를 입력받을 때 다음과 같은 제약을 주고자 합니다.

- 최소한 `5`자리 이상의 길이를 가져야 한다.
- 최소한 `1`개 이상의 숫자가 포함되어야 한다.
- 최소한 `1`개 이상의 대문자가 포함되어야 한다.

이 조건을 만족하는지 여부를 반환하는 프로그램을 구현하시오.

## 입력설명

- `0 < s.length <= 1000`

## 매개변수 형식

`s = "zer0Bas3`

## 반환값 형식

`true`

[*** 풀이 (Python) (100/100) ***]
'''

def solution(param0):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    alpha = ['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    final = []
    answer = True

    if len(param0) < 5:
        answer = False
        final.append(answer)
    else:
        answer = True
        final.append(answer)
    for i in range(len(nums)):
        if str(nums[i]) in param0:
            answer = True
            break
        else:
            answer = False
    final.append(answer)

    for i in range(len(alpha)):
        if alpha[i] in param0:
            answer = True
            break
        else:
            answer = False
    final.append(answer)

    for i in range(len(final)):
        if False in final:
            answer = bool(0)
            break
        else:
            answer = bool(1)
    
    return answer

'''
모범답안

from string import ascii_uppercase


def solution(s):
    if len(s) < 5:
        return False

    num_count = 0
    upper_count = 0

    for c in s:
        if c in ascii_uppercase:
            upper_count += 1
        if c in list('0123456789'):
            num_count += 1
        
        if num_count and upper_count:
            return True
    return False


'''