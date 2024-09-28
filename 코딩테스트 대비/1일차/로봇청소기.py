'''
## 문제

당신은 이번에 동아리에서 주최하는 로봇청소기 만들기 대회에 참가하게 되었다.

당신은 복잡한 알고리즘을 만들기에 앞서, 단순한 로봇을 만들어 동작을 실험해보려 한다.

당신이 만든 기초적인 로봇청소기의 동작은 다음과 같다.

- `(0, 0)` 좌표에서 오른쪽을 보고 출발한다.
    - `(0, 0)` 좌표에서 `(0, 1)` 좌표를 바라본 방향을 오른쪽으로 한다.
- 아래 스텝을 반복한다.
    - 현재 위치를 청소한다.
    - 바로 앞으로 이동할 수 있으면 이동한다.
    - 바로 앞으로 이동할 수 없으면 시계방향으로 90도 회전한다.

당신은 로봇청소기를 2차원 정수 배열로 표현된 `board`에서 테스트하려 한다.

`board[i][j]`에는 `(i, j)` 좌표의 상태가 기록되어 있으며, 이 상태는 아래와 같다.

- `0`: 청소를 해야 하는 일반 바닥
- `1`: 로봇청소기가 통과할 수 없는 장애물

이 때, 청소가 되는 칸의 수를 정수로 반환하시오.

## 입력설명

- `0 < board.length <= 100`
- `0 < board[i].length <= 100`

## 매개변수 형식

board = {{0, 0, 0, 0},
         {0, 1, 1, 0},
         {0, 0, 0, 0},
         {1, 0, 1, 1}}

## 반환값 형식

10

[*** 풀이 (Python) (40/100) ***]
'''

def bfs(i, j, n, m, board):
    q = []
    visited =[[0] * m for _ in range(n)]
    q.append((i, j))
    visited[i][j] = 0
    count = 1

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0
    while q:
        ci, cj = q.pop(0)
        if 0 <= ci < n and 0 <= cj < m and board[ci][cj] == 1 and visited[ci][cj] == 1:
            break
        elif (ci, cj) == (0, 0) and visited[ci][cj] == 1:
            break

        else:
            ni = ci + di[k]
            nj = cj + dj[k]

            if 0 <=ni < n and 0 <= nj < m and board[ni][nj] == 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1
                count += 1

            else:
                k = (k + 1) % 4
                ni = ci + di[k]
                nj = cj + dj[k]
                q.append((ni, nj))
                visited[ni][nj] = 1
                count += 1

    return count - 1

def solution(board):
    n = len(board)
    m = len(board[0])
    i, j = 0, 0

    return bfs(i, j, n, m, board)

'''
모범 답안

def solution(board):
    visited = {}
    i, j = 0, 0
    dir = 0
    
    N = len(board)
    M = len(board[0])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while not((i, j) in visited and visited[(i, j)][dir]):
        if (i, j) not in visited:
            visited[(i, j)] = [False for _ in range(4)]
        visited[(i, j)][dir] = True

        di, dj = directions[dir]
        next_i, next_j = i + di, j + dj
        
        if 0 <= next_i < N \
            and 0 <= next_j < M \
            and board[next_i][next_j] == 0:
            i, j = next_i, next_j
        else:
            dir = (dir + 1) % len(directions)
        
    return len(visited)


'''