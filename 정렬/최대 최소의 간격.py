N = int(input())

for n in range(N):
    T = int(input())
    arr = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0
    for i in range(T):
        if arr[min_idx] > arr[i]:
            min_idx = i

    for i in range(len(arr)):
        if arr[max_idx] <= arr[i]:
            max_idx = i

    if max_idx > min_idx:
        answer = max_idx - min_idx
    else:
        answer = min_idx - max_idx

    print(f'#{n+1} {answer}')