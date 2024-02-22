'''
N*N 인 2차원 배열 내부에 1로 채워진 사각 영역이 있다.
사각형의 가로, 세로 칸 수를 곱한 값을 출력하는 프로그램을 구하시오
사각형이 여러개인 경우 가장 큰 곱을 출력한다.
'''

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0
    for i in range(N):
        for j in range(N):
            ni, nj = i, j
            width = 0
            height = 0
            while 0 <= nj < N and arr[i][nj] != 0: # 현재 위치에 1이 있고 범위 내이면
                nj += 1 # 오른쪽으로 한칸 이동
            width = nj - j  # 가로 길이

            while 0 <= ni < N and arr[ni][j] != 0:
                ni += 1 # 왼쪽으로 한칸 이동
            height = ni - i # 세로 길이

            if max_count < width * height:
                max_count = width * height
            # 지나온 길 초기화!
            for p in range(i, i+ width):
                for q in range(j, j+height):
                    arr[p][q] = 0

    print(f'#{tc+1} {max_count}')