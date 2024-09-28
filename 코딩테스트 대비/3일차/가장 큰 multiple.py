'''
## 문제

양의 정수로 이루어진 배열 `nums`가 주어져 있다.

서로 다른 인덱스 `i`와 `j`를 선택하여 만들 수 있는 최대의 `(nums[i] - 1) * (nums[j] - 1)` 값을 구하시오.

## 입력설명

- `0 < nums.length <= 10000`

## 출력설명

가능한 가장 큰 값을 정수로 반환

## 매개변수 형식

`nums = {3, 5, 7, 5}`

## 반환값 형식

`24`

## 입출력 예시 설명

`i=2`, `j=3`이면, `(7-1)*(5-1)=24`로 가장 큰 값이 된다.

[*** 풀이 (Python) (100/100) ***]
'''

def solution(nums):
    first = max(nums)
    for i in range(len(nums)):
        if nums[i] == first:
            ans = i
    nums.pop(ans)
    second = max(nums)
    answer = (first -1 ) * (second -1)
    return answer

'''
모범답안
def solution(nums):
    max1 = -float('inf')
    max2 = -float('inf')

    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    
    return (max1-1)*(max2-1)


nums = [3, 5, 7, 5]
print(solution(nums))
'''