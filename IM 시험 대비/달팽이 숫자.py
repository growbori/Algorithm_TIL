T = int(input())
for tc in range(T):
    N = int(input())
    arr= [[0] * N for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    i = 0
    j = 0
    k = 0
    count = 1
    arr[0][0] = 1

    while count < N * N:
        nx = i + dx[k]
        ny = j + dy[k]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] != 0:
            k = (k+1) % 4
            nx = i + dx[k]
            ny = j + dy[k]

        i = nx
        j = ny
        count += 1
        arr[nx][ny] = count

    print(f'#{tc+1}')
    for idx in range(N):
        print(*arr[idx])


