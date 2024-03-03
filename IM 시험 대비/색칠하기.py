T = int(input())
for tc in range(T):
    N = int(input())
    arr= [list(map(int, input().split())) for _ in range(N)]
    board = [[0] * 10 for _ in range(10)]

    for i in range(N):
        a = arr[i][0]
        b = arr[i][1]
        c = arr[i][2]
        d = arr[i][3]
        e = arr[i][4]
        for i in range(a, c + 1):
            for j in range(b, d+1):
                board[i][j] += e

    result = 0
    for x in range(10):
        for y in range(10):
            if board[x][y] >= 3:
                result += 1

    print(f'#{tc+1} {result}')