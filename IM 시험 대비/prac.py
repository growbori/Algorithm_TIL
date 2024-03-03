board = [list(map(int, input().split())) for _ in range(5)]
play = [list(map(int, input().split())) for _ in range(5)]

call = []
for i in play:
    for x in i:
        call.append(x)

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, -1, 1, -1, 1]
total = 0
check = 0

for num in call:
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = 0
                check += 1
                cnt = 0
                if board[i][j] == 0:
                    for k in range(8):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < 5 and 0 <= ny < 5 and board[nx][ny] == 0:
                            cnt += 1
                if cnt >= 5:
                    total += 1

if total >= 3:
    print(check)