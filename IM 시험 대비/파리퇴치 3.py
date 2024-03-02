'''
최대한 많은 파리를 잡으려고 한다.
+, x 형태로 분사된다.
'''
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    ux = [1, 1, -1, -1]
    uy = [-1, 1, 1, -1]
    max_count = 0
    for i in range(N):
        for j in range(N):
            count = arr[i][j]
            for p in range(1, M):
                for k in range(4):

                    nx = i + dx[k] * p
                    ny = j + dy[k] * p

                    if 0 <= nx < N and 0 <= ny < N:
                        count += arr[nx][ny]
            if max_count < count:
                max_count = count

            count = arr[i][j]
            for p in range(1, M):
                for k in range(4):
                    nx = i + ux[k] * p
                    ny = j + uy[k] * p

                    if 0 <= nx < N and 0 <= ny < N:
                        count += arr[nx][ny]
            if max_count < count:
                max_count = count
    print(f'#{tc+1} {max_count}')