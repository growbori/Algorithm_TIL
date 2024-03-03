T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1, 1, 1, -1, -1]
    dy = [1, 0, -1, 0, -1, 1, -1, 1]
    total = 0
    for i in range(N):
        for j in range(M):
            count = 0
            for k in range(8):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] < arr[i][j]:
                    count += 1
            if count >= 4:
                total += 1

    print(f'#{tc+1} {total}')