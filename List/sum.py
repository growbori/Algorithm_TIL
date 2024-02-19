'''
100 * 100 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하여라
'''

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    diagonal_sum = 0
    diagonal_reverse_sum = 0
    max_sum = 0

    for i in range(100):
        horizon_sum = 0
        vertical_sum = 0
        for j in range(100):
            horizon_sum += arr[i][j]
            vertical_sum += arr[j][i]

        if max_sum < horizon_sum:
            max_sum = horizon_sum

        if max_sum < vertical_sum:
            max_sum = vertical_sum

        diagonal_sum += arr[i][i]
        diagonal_reverse_sum += arr[i][99-i]

    if max_sum < diagonal_sum:
        max_sum = diagonal_sum

    if max_sum < diagonal_reverse_sum:
        max_sum = diagonal_reverse_sum

    print(max_sum)