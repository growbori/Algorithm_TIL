'''
## 문제

정수로 이루어진 배열 `nums`가 있다. 이 배열에서 Longest increasing subsequence(LIS)의 길이를 출력하시오.

이 문제에서 LIS는 다음 조건을 만족하는 가장 긴 배열을 말한다.

- LIS는 엄격하게 증가하는 수열이어야 한다. 즉, `i < j` 이면 `arr[i] < arr[j]`이다.
- LIS는 원 배열 `nums`에서 일부 원소를 제거하여 만든다. 단, 원 배열의 원소의 순서는 그대로 유지해야 한다.

예를 들면, `nums = {6, 2, 4, 6, 11, 9, 9, 10}`일 때, 이 배열의 LIS는 `{2, 4, 6, 9, 10}`이 된다.

## 입력설명

- `0 < nums.length <= 10000`

## 출력설명

LIS의 길이를 정수로 반환

## 매개변수 형식

`nums = {6, 2, 4, 6, 11, 9, 9, 10}`

## 반환값 형식

`5`

[*** 풀이 (Python) (100/100) ***]
'''

def solution(nums):
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

'''
모범 답안

import sys
sys.setrecursionlimit(10**6)

def solution(nums):
    n = len(nums)
    dp = [[-1 for _ in range(n+1)] for _ in range(n)]

    def solve(curr, prev):
        if curr == n:
            return 0
        
        if dp[curr][prev + 1] != -1:
            return dp[curr][prev + 1]
        
        not_take = 0 + solve(curr + 1, prev)
        take = 0

        if prev == -1 or nums[curr] > nums[prev]:
            take = 1 + solve(curr + 1, curr)
        
        dp[curr][prev + 1] = max(take, not_take)
        return dp[curr][prev + 1]

    return solve(0, -1)

'''