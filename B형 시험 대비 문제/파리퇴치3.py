'''
N * N 배열 안의 숫자는 해당 영역에 존재하는 파리의 수 의미
스프레이를 뿌리는 경우 +, x 중 하나로 분사된다.
'''



T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    ux = [1, 1, -1, -1]
    uy = [-1, 1, 1, -1]
    max_count = 0
    for i in range(N):
        for j in range(N):
            count = fly_list[i][j]

            for p in range(1, M):
                for k in range(4):
                    nx = i + dx[k] * p
                    ny = j + dy[k] * p

                    if 0 <= nx < N and 0 <= ny < N:
                        count += fly_list[nx][ny]

            if max_count < count:
                max_count = count

            count = fly_list[i][j]  # count 값 초기화
            for p in range(1, M):
                for k in range(4):
                    nx = i + ux[k] * p
                    ny = j + uy[k] * p

                    if 0 <= nx < N and 0 <= ny < N:
                        count += fly_list[nx][ny]

            if max_count < count:
                max_count = count
                
    print(max_count)