'''
## 문제

두 명의 플레이어가 경쟁하는 게임이 있다.

이 게임은 시작할 때 여러 개의 돌을 내려 놓는다. 각 돌은 두 플레이어에게 서로 다른 가치를 가진다.

`i`번째 돌이 각 플레이어에게 주는 가치는 `value[i][0]`, `value[i][1]`에 양의 정수로 주어진다.

첫번째 플레이어부터 순서대로 돌아가면서 하나씩 돌을 선택하여 가져가며, 최종 점수는 각 플레이어의 돌의 가치의 합이다.

각 플레이어는 양 플레이어에게 주는 돌의 가치를 모두 알고 있고, 최선의 선택을 한다고 하자.

이 때 경기가 끝날 때 그 결과를 `1`(첫번째 플레이어 승리), `0`(동점), `-1`(두번째 플레이어 승리) 출력하시오.

## 입력설명

- `0 < value.length <= 10000`
- `0 < value[i][0] <= 100`
- `0 < value[i][1] <= 100`

## 매개변수 형식

`value = {{5, 3}, {6, 9}, {4, 5}, {6, 3}, {2, 8}, {5, 4}}`

## 반환값 형식

`1`

## 예시 입출력 설명

아래 순서로 선택하는 것이 각자 최선의 선택이며, 첫 번째 플레이어가 승리한다.

| 차례 | 선택 | 플레이어1 점수 | 플레이어2 점수 |
| --- | --- | --- | --- |
| 플레이어1 | {6, 9} | 6 | 0 |
| 플레이어2 | {2, 8} | 6 | 8 |
| 플레이어1 | {6, 3} | 12 | 8 |
| 플레이어2 | {5, 4} | 12 | 12 |
| 플레이어1 | {4, 5} | 16 | 12 |
| 플레이어2 | {5, 3} | 16 | 15 |

[*** 풀이 (Python) (50/100) ***]
'''

def solution(value):
    player1 = 0
    player2 = 0
    value.sort(key=lambda x: x[1], reverse=True)
    while len(value) > 0:
        # 첫 번째로 큰 값을 찾음
        first = max(value, key=lambda x: x[0])
        player1 += first[0]
        value.remove(first)

        if len(value) > 0:
            # 두 번째로 큰 값을 찾음
            second = max(value, key=lambda x: x[1])
            player2 += second[1]
            value.remove(second)  

    if player1 > player2:
        answer = 1
    elif player1 == player2:
        answer = 0
    else:
        answer = -1
    return answer

'''
모범답안

from heapq import heappush, heappop

def solution(value):
    heap = []
    for v in value:
        heappush(heap, (-(v[0] + v[1]), v[0], v[1]))
    
    total_value = 0
    turn = 0
    while heap:
        _, v1, v2 = heappop(heap)
        if turn % 2 == 0:
            total_value += v1
        else:
            total_value -= v2
        turn += 1
    
    return 1 if total_value > 0 else -1 if total_value < 0 else 0
'''