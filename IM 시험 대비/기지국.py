T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # A 주위 기지국 X로 변경
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                for p in range(1, 2):
                    for k in range(4):
                        nx = i + dx[k] * p
                        ny = j + dy[k] * p
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                            arr[nx][ny] = 'X'

    # B 주위 기지국 X로 변경
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'B':
                for p in range(1, 3):
                    for k in range(4):
                        nx = i + dx[k] * p
                        ny = j + dy[k] * p
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                            arr[nx][ny] = 'X'

    # C 주위 기지국 X로 변경
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'C':
                for p in range(1, 4):
                    for k in range(4):
                        nx = i + dx[k] * p
                        ny = j + dy[k] * p
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                            arr[nx][ny] = 'X'

    result = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'H':
                result += 1

    print(result)
