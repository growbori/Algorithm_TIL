T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(1, M+1):
                if (i+j+2) == k or (i+j+2) % k == 0:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    elif arr[i][j] == 1:
                        arr[i][j] = 0
                elif M % k == 0:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    else:
                        arr[i][j] = 0
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                count += 1

    print(f'#{tc+1} {count}')