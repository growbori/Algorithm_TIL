T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    max_count = 0
    for i in range(N):
        for j in range(N):
            count = arr[i][j]
            for p in range(1, N):
                for k in range(4):
                    nx = i + dx[k] * p
                    ny = j + dy[k] * p

                    if 0 <= nx < N and 0 <= ny < N:
                        count += arr[nx][ny]
            if max_count < count:
                max_count = count

    print(f'#{tc+1} {max_count}')

