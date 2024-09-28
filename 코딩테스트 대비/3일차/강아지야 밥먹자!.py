'''
## 문제

당신은 머리가 `N`개 달린 멋진 강아지를 한마리 키우고 있다.

이 강아지는 먹이를 급여할때 손에 먹이를 들고 직접 머리에 급여해야 한다.

당신은 한 손에 하나씩 먹이를 들고 한 번에 `2`개의 머리까지 동시에 급여할 수 있다.

각 머리는 식사량이 다르며, `i`번째 머리에 급여해야 하는 횟수는 `food[i]`로 주어진다.

이 때, 모든 머리의 식사량을 채우려면 최소 몇번의 급여를 해야 하는지 구하시오.

## 입력설명

- `0 < N = food.length <= 10000`
- `0 < food[i] <= 1000`

## 출력설명

최소 급여 횟수를 정수로 반환

## 매개변수 형식

`food = {6, 3, 4, 5}`

## 반환값 형식

`9`

## 입출력 예시 설명

아래 순서대로 `9`번 급여하면 된다.

- `0`번 머리와 `3`번 머리에 `5`번 급여
- `0`번 머리와 `2`번 머리에 `1`번 급여
- `1`번 머리와 `2`번 머리에 `3`번 급여


[*** 풀이 (Python) (50/100) ***]
'''

def solution(food):
    count = 0
    while True :
        if len(food) == 0:
            break
        elif len(food) == 1:
            count += food[0]
            break
        else:
            first = max(food)
            for i in range(len(food)):
                if first == food[i]:
                    food.pop(i)
                    break
            second = max(food)
            for i in range(len(food)):
                if second == food[i]:
                    food.pop(i)
                    break
            feed = min(first, second)
            if first == second:
                count += first
            elif first == feed:
                if (second-feed) != 0:
                    food.append(second-feed)
                    count += first
                else:
                    count += first
                    break
            else:
                if (first-feed) != 0:
                    food.append(first-feed)
                    count += second
                else:
                    count += second
                    break

    return count

'''
모범답안

def solution(food):
    food.sort(reverse=True)

    count = 0
    curr = food[0]
    for f in food[1:]:
        if f < curr:
            curr -= f
            count += f
        else:
            count += curr
            curr = f - curr
    count += curr
    return count


# food = [6, 3, 4, 5]
# print(solution(food))

'''