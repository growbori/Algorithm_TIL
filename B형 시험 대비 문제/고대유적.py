'''
구조물이 있는 곳은 1, 빈 땅은 0으로 표시된다.
구역에서 가장 긴 구조물의 길이를 구하시오
'''

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 0:
                cnt = 0
            else:
                cnt += arr[i][j]
                if max_v < cnt:
                    max_v = cnt

    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 0:
                cnt = 0
            else:
                cnt += arr[i][j]
                if max_v < cnt:
                    max_v = cnt


    print(f'#{tc+1} {max_v}')