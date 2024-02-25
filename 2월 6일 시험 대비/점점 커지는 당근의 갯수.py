T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_count = 0
    count = 1
    for i in range(N-1):
        if arr[i] < arr[i+1]:
            count += 1
        else:
            count = 1

        if max_count < count:
            max_count = count
    print(max_count)
