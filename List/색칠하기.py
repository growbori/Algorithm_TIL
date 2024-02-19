'''
10 * 10 격자에 빨간색과 파란색을 칠하고자 한다.
N개의 영역에 칠한 후 보라색이 겹쳐지는 부분을 구하시오
'''

T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    color_map = [[0] * 10 for _ in range(10)]
    for i in range(N):
        c1, a1, c2, a2, color = arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4]

        for x in range(c1, c2+1):
            for y in range(a1, a2+1):
                color_map[x][y] += color
    result = 0
    for i in range(10):
        for j in range(10):
            if color_map[i][j] == 3:
                result += 1

    print(result)

