T = int(input())
for tc in range(T):
    N = int(input())
    arr = [[1] * (i+1) for i in range(N)]

    for i in range(len(arr)):
        for j in range(i):
            if j != 0 and i != j:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    print(f'#{tc+1}')
    for i in range(N):
        print(*arr[i])
