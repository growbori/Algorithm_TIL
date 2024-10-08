'''
## 문제

하나의 문장 `s`가 당신에게 주어져 있다. 이 문장을 단어별로 구분하여 전광판에 최대한 여러번 반복하려 한다.

전광판의 크기는 `M`x`N`의 크기로 주어지며, 문장은 단어를 순서대로 쓰되, 단어끼리는 공백이나 다음 줄로 구분되어야 한다.

또한, 한 단어는 반드시 한 줄 이내에 적혀야 한다.

예를 들어, `i love zerobase`라는 문장이 주어져 있고, `5`x`9` 크기의 전광판이 주어졌다고 하자.

이 경우 아래와 같이 최대 `2`번 반복이 가능하다. 알아보기 쉽게 하기 위해 공백 대신 `^`로 표기하였다.

```
i^love^^^
zerobase^
i^love^^^
zerobase^
i^love^^^
```

주어진 `s`, `M`, `N`에 대하여 최대로 문장을 반복할 수 있는 횟수를 구하시오.

## 입력설명

- `0 <= s.length() <= 100000`
- `0 < M <= 10000`
- `0 < N <= 10000`

## 매개변수 형식

`s = "i want to study more"`

`M = 7`

`N = 7`

## 반환값 형식

`2`

[*** 풀이 (Python) (100/100) ***]
'''

def solution(s, M, N):
    # 입력 문자열 s에 공백을 추가하여 단어 사이의 구분을 명확히 함
    s = s + ' '

    # infinite_index: 전광판에서 반복하여 문장을 쓸 때, 몇 번째 문자인지를 추적
    # l: 문자열 s의 길이
    # row: 전광판에서 현재 몇 번째 줄에 있는지를 추적
    infinite_index, l, row = 0, len(s), 0

    # row가 M(전광판의 줄 수)보다 작을 동안 반복
    while row < M:
        # 만약 infinite_index가 s의 길이로 나누어떨어지고, 현재 row가 0이 아니면 (즉, 한 번 이상 반복이 끝난 경우)
        if infinite_index % l == 0 and row > 0: 
            # 한 줄이 완전히 반복되었으므로, 전체 전광판의 크기를 나눠 반복할 수 있는 횟수를 계산
            infinite_index *= M // row
            # 나머지 줄(row)와 남은 전광판 크기(M)을 재설정
            row, M = 0, M % row
        else:
            # 현재 줄에서 s를 전광판 N 크기만큼 늘려 쓸 수 있는 만큼 증가
            infinite_index += N
            # 단어가 끝나기 전까지 뒤로 한 글자씩 이동 (단어를 쪼개지 않기 위해)
            while s[infinite_index % l] != ' ':
                infinite_index -= 1
            # 단어가 끝난 후 다시 앞 한 칸으로 이동
            infinite_index += 1
            # 다음 줄로 이동
            row += 1

    # 전체 전광판에 문장을 반복한 횟수 계산 후 반환
    return infinite_index // l

'''
문제 풀이 답변과 모범 답안이 같음
문제 풀이 꼭! 다시 보면서 이해하기!
'''