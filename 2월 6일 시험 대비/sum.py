for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    diagonal = 0
    diagonal_rev = 0
    for i in range(100):
        vertical = 0
        horizon = 0
        for j in range(100):
            vertical += arr[i][j]
            horizon += arr[j][i]

        if max_sum < vertical:
            max_sum = vertical

        if max_sum < horizon:
            max_sum = horizon

        diagonal += arr[i][i]
        diagonal_rev += arr[99-i][i]

    if max_sum < diagonal:
        max_sum = diagonal

    if max_sum < diagonal_rev:
        max_sum = diagonal_rev

    print(max_sum)

