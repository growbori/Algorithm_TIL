for tc in range(10):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for j in range(N):
        magnet = []
        for i in range(N):
            if table[i][j] == 1 or table[i][j] == 2:
                magnet.append(table[i][j])

        previous = 0
        while magnet:
            now = magnet.pop()
            if previous == 2 and now == 1:
                cnt += 1
            previous = now

    print(cnt)
