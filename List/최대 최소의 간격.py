'''
최대값의 위치와 최소값의 위치의 차이를 절댓값으로 출력하시오.
가장 작은 수가 여러개이면 먼저 나오는 위치로 하고 가장 큰 수가 여러개이면 마지막으로 나오는 위치로 한다.
'''

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    min_idx = 0
    max_idx = 0
    for i in range(len(arr)):
        if arr[min_idx] > arr[i]:
            min_idx = i

        if arr[max_idx] <= arr[i]:
            max_idx = i

    print(abs(max_idx - min_idx))
