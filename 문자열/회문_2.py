

for tc in range(1, 11):
    T = int(input())
    arr = [input() for _ in range(8)]
    count = 0

    # 가로 탐색

    for i in range(8):
        for j in range(8-T+1):
            if arr[i][j: j+ T] == arr[i][j: j + T][::-1]: # j: j 문자열 크기 그대로 유지!
                count += 1

    # 세로 탐색
    for i in range(8 - T + 1):
        for j in range(8):
            vertical = ''
            for x in range(i, i + T):
                vertical += arr[x][j]
            if vertical == vertical[::-1]:
                count += 1

    print(f'#{tc} {count}')


