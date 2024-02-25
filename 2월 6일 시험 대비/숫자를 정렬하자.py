T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(len(arr)-1):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    print(f'#{tc+1}', *arr)