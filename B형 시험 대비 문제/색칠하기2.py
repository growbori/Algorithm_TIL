'''
10*10 격자에 빨간색과 파란색을 칠하고자 한다.
칠이 끝난 후 빨간색 영역과 파란색 영역의 외곽 길이를 구하는 프로그램을 구하시오
=> 두 사각형 외곽의 길이 합을 구하면 됨
'''

T = int(input())
for tc in range(T):
    N = int(input())
    color_map = [[0] * 10 for _ in range(10)]

    for _ in range(N):
        c1, a1, c2, a2, color = list(map(int, input().split()))

        for i in range(c1, c2+1):
            for j in range(a1, a2+1):
                color_map[i][j] += color

    total = 0
    for i in range(10):
        for j in range(10):
            if color_map[i][j] == 1 or color_map[i][j] == 2:
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < 10 and 0 <= nj < 10 and color_map[i][j] != color_map[ni][nj]:
                        total += 1
                    elif ni < 0 or ni >= 10 or nj < 0 or nj >= 10:
                        total += 1

    print(f'#{tc+1} {total}')