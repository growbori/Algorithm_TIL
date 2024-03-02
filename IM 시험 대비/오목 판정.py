T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    dx = [0, 1, 1, 1]
    dy = [1, 1, 0, -1]
    answer = 'NO'
    for i in range(N):
        for j in range(N):
            for k in range(4):
                if arr[i][j] == 'o':
                    count = 1
                    nx = i + dx[k]
                    ny = j + dy[k]

                    while 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                        count += 1
                        nx = nx + dx[k]
                        ny = ny + dy[k]

                    if count == 5:
                        answer = 'YES'


    print(f'#{tc+1} {answer}')