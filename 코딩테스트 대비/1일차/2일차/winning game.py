'''
## 문제

당신은 이기는 게임만 플레이하는 항상 이기는 게이머다.

플레이하고자 하는 게임은, 모든 스테이지를 클리어한 후에 체력이 `0`보다 크면 이기는 게임이다.

각 스테이지에서 플레이어가 받는 데미지는 `damages`에 정수 배열로 주어진다.

플레이어는 `i`번째 스테이지를 클리어할 때 `damages[i]`의 데미지를 입지만, `shield`만큼의 데미지를 감소시켜준다.

예를 들어, `shield = 3`이면 데미지 `5`를 받았을 때 실제 체력이 감소하는 양은 `2`이다.

그리고 데미지 `2`인 경우 데미지를 완전히 방어하여 체력이 `0`만큼 감소한다.

이 게임을 이기기 위해서 필요한 플레이어의 최소 체력을 구하시오.

## 입력설명

- `0 < damages.length <= 10000`
- `0 < damages[i] <= 1000`
- `0 <= shield <= 1000`

## 출력설명

게임을 이기기 위해 필요한 최소 체력을 정수로 반환

## 매개변수 형식

`damages = {5, 3, 6, 2, 4}`

`shield = 4`

## 반환값 형식

`4`

[*** 풀이 (Python) (100/100) ***]
'''

def solution(damages, shield):
    health = 1
    for i in range(len(damages)):
        if damages[i] >= shield:
            health += damages[i] - shield
        else:
            health += 0
    return health

'''
모범답안

def solution(damages, shield):
    life = 1
    for d in damages:
        life += max(0, d - shield)
    return life
'''