T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = 0
    min_num = 10000000
    for i in range(N):
        if max_num < arr[i]:
            max_num = arr[i]

    for i in range(N):
        if min_num > arr[i]:
            min_num = arr[i]

    print(max_num - min_num)