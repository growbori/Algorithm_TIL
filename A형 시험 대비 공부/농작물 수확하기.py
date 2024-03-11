'''
농장의 크기는 항상 홀수
수확은 농장 크기에 딱 맞는 정사각형 마름모 형태로만
'''

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    M = N//2
    # for i in range(N):
    #     if i <= M:
    #         for j in range(M-i, M+i+1):
    #             ans += arr[i][j]
    #     else:
    #         for j in range(i-M, N-(i-M)):
    #             ans += arr[i][j]
    s = e = M
    for i in range(N):
        for j in range(s, e+1):
            ans += arr[i][j]

        if i < M:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print(f'#{tc+1} {ans}')

