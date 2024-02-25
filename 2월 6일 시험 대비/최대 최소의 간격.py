T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0
    max_idx = 0
    for i in range(N):
        if arr[min_idx] <= arr[i]:
            min_idx = i

        if arr[max_idx] > arr[i]:
            max_idx = i

    print(abs(max_idx-min_idx))