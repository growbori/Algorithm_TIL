T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0

    for i in range(N):
        count = 0
        for j in range(M):
            if arr[i][j] == 0:
                count = 0
            else:
                count += arr[i][j]
                if max_count < count:
                    max_count = count

    for j in range(N):
        count = 0
        for i in range(N):
            if arr[i][j] == 0:
                count = 0
            else:
                count += arr[i][j]
                if max_count < count:
                    max_count = count

    print(max_count)