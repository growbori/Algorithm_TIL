'''
## 문제

정수로 이루어진 배열 `nums`가 주어졌다.

이 배열에 아래 연산을 적용하려고 한다.

- 배열의 요소가 양 옆의 값보다 작으면 `1` 증가시킨다.
- 배열의 요소가 양 옆의 값보다 크면 `1` 감소시킨다.
- 양 끝에 위치한 요소는 변하지 않는다.

위 연산을 적용했을 때 배열에 변화가 생기면 이 배열은 '불안정하다'고 하고,

배열에 변화가 생기지 않으면 '안정하다'고 하자.

배열이 안정해질 때 까지 위 연산을 적용한 결과를 출력하시오.

## 입력설명

- `3 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`

## 출력설명

안정해진 배열을 정수 배열로 반환

## 매개변수 형식

`nums = {10, 8, 6, 7, 5}`

## 반환값 형식

`{10, 8, 7, 6, 5}`

## 예제입출력 설명

주어진 배열은 연산을 한번 적용하면 안정된 배열이 된다.

`{10, 8, 6, 7, 5}` -> `{10, 8, 7, 6, 5}`

[*** 풀이 (Python) (100/100) ***]
'''

def solution(nums):
    while True:
        check = [0] * len(nums)
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                check[i] -= 1
            elif nums[i-1] > nums[i] and nums[i+1] > nums[i]:
                check[i] += 1

        result = []
        for i in range(len(nums)):
            result.append(nums[i] + check[i])

        total = 0
        for i in range(len(check)):
            if check[i] != 0:
                total += 1

        if total == 0:
            ans = result
            break
        else :
            nums = result
    return ans


'''
모범답안

def solution(nums):
    new_nums = nums.copy()

    while True:
        is_changed = False
        for i in range(1, len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                new_nums[i] = nums[i] - 1
                is_changed = True
            elif nums[i-1] > nums[i] and nums[i] < nums[i+1]:
                new_nums[i] = nums[i] + 1
                is_changed = True
            else:
                new_nums[i] = nums[i]
            
        if not is_changed:
            return nums
        
        nums = new_nums.copy()

'''