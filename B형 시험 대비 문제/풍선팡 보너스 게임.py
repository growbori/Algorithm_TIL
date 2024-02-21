'''
N*N 격자 안에 풍선을 터뜨리면 같은 행과 열의 풍선이 모두 터진다.
이때 얻을 수 있는 최대 점수를 출력하라
'''

T = int(input())
for tc in range(T):
    N = int(input())
    ball_list = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    max_count = 0
    for i in range(N):
        for j in range(N):
            count = ball_list[i][j]
            for p in range(1, N):   # 1부터 N까지 범위 유의하기!
                for k in range(4):
                    nx = i + dx[k] * p
                    ny = j + dy[k] * p

                    if 0 <= nx < N and 0 <= ny < N:
                        count += ball_list[ nx][ny]

            if max_count < count:
                max_count = count

    print(max_count)
