dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]
op = [0, 2, 1]
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    play = [list(map(int, input().split())) for _ in range(M)]
    board = [[0] * N for _ in range(N)]

    B = 1
    W = 2

    board[N//2-1][N//2-1] = W
    board[N//2-1][N//2] = B
    board[N//2][N//2] = W
    board[N//2][N//2-1] = B

    for i, j, wb in play:
        board[i-1][j-1] = wb

        for k in range(8):
            nx = i-1 + dx[k]
            ny = j-1 + dy[k]
            flip = []

            while 0 <= nx < N and 0 <= ny < N and board[nx][ny] == op[wb]:
                flip.append((nx, ny))
                nx = nx + dx[k]
                ny = ny + dy[k]

                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == wb:
                    for p, q in flip:
                        board[p][q] = wb

    cnt_b = 0
    cnt_w = 0

    for x in range(N):
        for y in range(N):
            if board[x][y] == B:
                cnt_b += 1
            elif board[x][y] == W:
                cnt_w += 1

    print(f'#{tc+1} {cnt_b} {cnt_w}')
