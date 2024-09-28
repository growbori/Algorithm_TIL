'''
## 문제

문자열로 이루어진 배열 `words`에는 겹치지 않는 여러 문자열이 주어져 있다.

이 문자열 중에 `i`번째 문자열과 `j`번째 문자열을 `words[i] + words[j]`와 같이 이어 붙여서 회문문자열이 되는 경우의 수를 구하시오.

단, `i != j`이며, 회문 문자열은 거꾸로 뒤집어도 똑같은 문자열을 말한다.

## 입력설명

- `0 < words.length <= 1000`
- `0 <= words[i].length <= 100`

## 매개변수 형식

`words = {"zero", "base", "esab", "esabe", "orez"}`

## 반환값 형식

`5`

## 예시 입출력 설명

아래 총 `5`가지 경우에 회문 문자열이 된다.

- `i=0, j=4`: `"zeroorez"`
- `i=1, j=2`: `"baseesab"`
- `i=1, j=3`: `"esabebase"`
- `i=2, j=1`: `"esabbase"`
- `i=4, j=0`: `"orezzero"`

[*** 풀이 (Python) (100/100) ***]
'''

def solution(words):
    count = 0
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                new_word = words[i] + words[j]
                if new_word == new_word[::-1]:
                    count += 1
    return count

'''
모범답안

def solution(damages, shield):
    life = 1
    for d in damages:
        life += max(0, d - shield)
    return life


'''