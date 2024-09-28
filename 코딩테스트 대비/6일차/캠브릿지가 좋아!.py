'''
## 문제

사람은 한 단어 내에서는 첫 글자와 마지막 글자가 맞으면, 나머지 문자의 순서가 달라도 단어를 이해할 수 있다고 한다.

예를 들어,

`"캠브릿지 대학의 연구결과"`

위 문장을 아래와 같이 써도 잘 이해가 된다는 것이다.

`"캠릿브지 대학의 연결구과"`

정상적인 문자열 `s`가 주어졌을 때, 문자열 `t`가 이러한 효과에 의해 잘 이해가 되는지 여부를 판단하는 프로그램을 작성하시오.

단, 여기서 '단어'는 공백으로 구분된 문자열을 이야기한다.

## 입력설명

- `0 < s.length <= 10000`
- `0 < t.length <= 10000`

## 출력설명

문자열 `t`가 올바르게 이해되는지 여부를 논리형으로 반환

## 매개변수 형식

`s = "캠브릿지 대학의 연구결과에 따르면"`

`t = "캠릿브지 대학의 연결과구에 따르면"`

## 반환값 형식

`true`

[*** 풀이 (Python) (100/100) ***]
'''

def solution(s, t):
    case = []
    word = ''
    for i in range(len(s)):
        if s[i] != ' ':
            word += s[i]
        else:
            case.append(word)
            word = ''
    case.append(word)

    compare = []
    text = ''
    for i in range(len(t)):
        if t[i] != ' ':
            text += t[i]
        else:
            compare.append(text)
            text = ''
    compare.append(text)

    answer = True
    for i in range(len(case)):
        if case[i][0] != compare[i][0]:
            answer = False
        if case[i][-1] != compare[i][-1]:
            answer = False
    return answer

'''
모범답안

def solution(s, t):
    if len(s) != len(t):
        return False

    for s_, t_ in zip(s.split(' '), t.split(' ')):
        if len(s_) != len(t_):
            return False
        if len(s_) < 3 and s_ != t_:
            return False
        if not (s[0] == t[0] and s[-1] == t[-1]):
            return False
        if sorted(list(s_[1:-1])) != sorted(list(t_[1:-1])):
            return False
    return True


'''