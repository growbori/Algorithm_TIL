T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            count = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    count += arr[x][y]
            if max_count < count:
                max_count = count

    print(f'#{tc+1} {max_count}')