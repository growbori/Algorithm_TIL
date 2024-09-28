'''
## 문제

두 벡터의 내적은 "같은 인덱스를 가진 요소의 곱의 총 합"으로 정의된다.

예를 들어 `x = {1, 2, 3}`, `y = {4, 5, 6}`일 때, 두 벡터의 내적은

`1*4 + 2*5 + 3*6 = 32`와 같이 계산할 수 있다.

한편, 희소 벡터는 대부분의 요소가 `0`이고 일부 요소만 `0`이 아닌 값을 가지는 벡터를 말한다.

우리는 일반 벡터 `x = {1, 0, 0, 3, 0, 2}`를 희소 벡터로 아래와 같이 표현하기로 하였다.

`x = {{0, 1}, {3, 3}, {5, 2}}`

즉, `x{i} = {인덱스, 값}`으로 `0`이 아닌 값만 표현하는 것이다.

희소 벡터 `x`와 `y`가 주어졌을 때, 두 벡터의 내적을 구하시오.

## 입력설명

- `0 < x.length <= 10000`
- `0 < y.length <= 10000`
- `0 <= x[i][0] <= 1000000`
- `0 <= y[i][0] <= 1000000`
- `10000 <= x[i][1] <= 10000`
- `10000 <= y[i][1] <= 10000`

## 매개변수 형식

`x = {{0, 1}, {3, 3}, {5, 2}, {6, 4}}`

`y = {{2, 5}, {5, 4}, {6, 2}}`

## 반환값 형식

`16`

[*** 풀이 (Python) (100/100) ***] -> 시간 초과 개선을 위해 투 포인터 사용!
'''

def solution(x, y):

    loc_x = 0
    loc_y = 0

    total = 0

    while loc_x < len(x) and loc_y < len(y):
        if x[loc_x][0] == y[loc_y][0]:
            total += x[loc_x][1] * y[loc_y][1]
            loc_x += 1
            loc_y += 1
        elif x[loc_x][0] < y[loc_y][0]:
            loc_x += 1
        else: 
            loc_y += 1

    return total

'''
case 2

def solution(x, y):
    vector = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i][0] == y[j][0]:
                vector += x[i][1] * y[j][1]
    return vector
'''

'''
모범답안

def solution(x, y):
    i = 0
    j = 0

    x.sort()
    y.sort()

    inner = 0
    while i < len(x) and j < len(y):
        if x[i][0] == y[j][0]:
            inner += x[i][1] * y[j][1]
        
        if x[i][0] < y[j][0]:
            i += 1
        else:
            j += 1
    return inner

'''