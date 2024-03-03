for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_count = 0
    diagonal_sum = 0
    diagonal_rev_sum = 0
    # 가로 탐색
    for i in range(100):
        vertical = 0
        horizon = 0
        for j in range(100):
            vertical += arr[i][j]
            horizon += arr[j][i]

        if max_count < vertical:
            max_count = vertical

        if max_count < horizon:
            max_count = horizon

    # 대각선 탐색
        diagonal_sum +=arr[i][i]
        diagonal_rev_sum += arr[99-i][i]

    if max_count < diagonal_sum:
        max_count = diagonal_sum

    if max_count < diagonal_rev_sum:
        max_count = diagonal_rev_sum

    print(f'#{tc+1} {max_count}')