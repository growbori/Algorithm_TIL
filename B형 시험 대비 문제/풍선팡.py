'''
풍선이 M 개씩 N 개의 줄에 있고, 풍선을 터뜨리면 안에 든 종이 꽃가루 개수 만큼
상하좌우의 풍선이 추가로 터짐
'''

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    ball_list = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    max_count = 0
    for i in range(N):
        for j in range(M):
            count = ball_list[i][j]

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    count += ball_list[nx][ny]

            if max_count < count:
                max_count = count
    print(max_count)