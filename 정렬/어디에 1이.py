T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range (N)]

    # 가로, 세로로 연속한 1의 개수가 K인  경우의 수

    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            else:
                if cnt == K:
                    ans +=1
                cnt = 0
    for j in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            else:
                if cnt == K:
                    ans +=1
                cnt = 0
    print(f'#{tc} {ans}')