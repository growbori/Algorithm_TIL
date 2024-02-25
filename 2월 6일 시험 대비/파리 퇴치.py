T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fly_list = []

    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_fly = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    sum_fly += arr[x][y]
                    fly_list.append(sum_fly)
    print(max(fly_list))
