'''
## 문제

`nums` 배열은 `1`부터 `N` 까지의 숫자로 이루어진 배열입니다. 하지만 중간 중간에 없는 순자가 있습니다. 비어 있는 갯수를 반환하시오.

- 배열의 구성 요소는 '자연수'만 포함됩니다.
- 배열의 구성 요소는 '중복 값이' 들어가지 않습니다 (유일한 자연수의 집합)

## 입력설명

- `0 < nums.length <= 10000`

## 출력 설명

배열에 포함되지 않은 숫자의 개수를 정수로 반환

## 예시 입출력1

`nums = {1, 2, 3, 4}`

출력: `0`

## 예시 입출력2

`nums = {1, 5, 6, 4}`

출력: `2`

[*** 풀이 (Python) (100/100) ***]
'''

def solution(param0):
    N = max(param0)
    check = []
    for i in range(1, N+1):
        check.append(i)
    count = 0
    for i in range(len(check)):
        if check[i] not in param0:
            count += 1
    print(check)
    print(param0)
    return count

'''
모범답안
def solution(nums):
    return max(nums) - len(nums)
'''