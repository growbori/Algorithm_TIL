'''
## 문제

배열 `nums`에 `0`이 아닌 정수가 있습니다. 이때 양의 정수 `K` 라고 할 경우 `K`와 `-K`가 모두 배열 내에 있다면 `K`를 출력하는 메소드를 작성하세요.

`K` 와 `-K` 쌍을 찾을수 없다면 `0`을 출력하고, 쌍이 여러개 있을 경우 가장 큰 `K`를 출력하세요.

## 입력설명

- `0 < nums.length <= 10000`

## 출력설명

가장 큰 `K`를 정수로 반환

## 매개변수 형식

`nums = {3, 2, -2, 5, -3}`

## 반환값 형식

`3`

[*** 풀이 (Python) (100/100) ***] -> 투포인터 활용해서 문제 풀이 성공!
'''
def solution(param0):
    param0.sort()
    left = 0
    right = len(param0)-1
    answer = 0
    while left < right:
        if param0[right] == -param0[left]:
            answer = param0[right]
            break
        elif param0[right] > -param0[left]:
            right -= 1
        else:
            left += 1

    return answer

'''
모범답안

function solution(nums) {
  let maxK = 0;
  const negSet = new Set(nums.filter((i) => i < 0));

  nums
    .filter((i) => i > 0)
    .forEach((i) => {
      if (negSet.has(-i)) {
        maxK = Math.max(maxK, i);
      }
    });

  return maxK;
}

'''