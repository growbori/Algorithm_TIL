T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    coloring = [[0] * 10 for _ in range(10)]

    for i in range(N):
        c1, a1, c2, a2, color = arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4]
        for i in range(c1, c2+1):
            for j in range(a1, a2+1):
                coloring[i][j] += int(color)


    count = 0
    for i in range(10):
        for j in range(10):
            if coloring[i][j] == 3:
                count += 1

    print(count)