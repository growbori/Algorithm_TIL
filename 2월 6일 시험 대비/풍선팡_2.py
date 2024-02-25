T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_count = 0
    for i in range(N):
        for j in range(M):
            sum_flower = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    sum_flower += arr[ni][nj]

            if max_count < sum_flower:
                max_count = sum_flower


    print(max_count)
