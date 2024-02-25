T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    max_count = 0

    for i in range(N):
        for j in range(M):
            count = arr[i][j]
            for p in range(1, arr[i][j]+1):
                for k in range(4):
                    nx = i + dx[k] * p
                    ny = j + dy[k] * p

                    if 0 <= nx < N and 0 <= ny < M:
                        count += arr[nx][ny]

            if max_count < count:
                max_count = count
    print(f'#{tc+1} {max_count}')