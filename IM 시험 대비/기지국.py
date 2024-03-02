'''
기지국에 커버되지 않는 집의 수를 구하고자 한다.
A, B, C를 기준으로 동서남북으로 1, 2, 3개를 커버하는 기지국이다. x인 원소는 아무것도 없다는 것을 의미
'''

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # A 근처 H제거
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                for p in range(1, 2):
                    for k in range(4):
                        nx = i + dx[k] * p
                        ny = j + dy[k] * p
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                            arr[nx][ny] = 'X'

    # B 근처 H제거
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'B':
                for p in range(1, 3):
                    for k in range(4):
                        nx = i + dx[k] * p
                        ny = j + dy[k] * p
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                            arr[nx][ny] = 'X'

    # C 근처 H제거
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'C':
                for p in range(1, 4):
                    for k in range(4):
                        nx = i + dx[k] * p
                        ny = j + dy[k] * p
                        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'H':
                            arr[nx][ny] = 'X'

    # H 갯수 카운트
    count = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                count += 1
    print(f'#{tc+1} {count}')