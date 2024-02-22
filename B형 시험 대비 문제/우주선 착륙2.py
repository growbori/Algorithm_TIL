T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0

    for i in range(N):
        for j in range(M):
            cnt = 0
            height = arr[i][j]

            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0], [1, -1], [1, 1], [-1, 1], [-1, -1]]:
                ni, nj = i + di, j + dj

                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] < arr[i][j]:
                    cnt += 1

            if cnt >= 4:
                total += 1
    print(f'#{tc+1} {total}')