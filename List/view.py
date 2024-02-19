'''
좌우로 2칸 이상 공백이 존재할 때 조망권이 확보된다.
조망권이 확보되는 수를 구하여라
'''

for tc in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(2, len(arr)-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i-2]:
            if arr[i] > arr[i+1] and arr[i] > arr[i+2]:
                answer += arr[i] - max(arr[i-1], arr[i-2], arr[i+1], arr[i+2])

    print(answer)
