T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    arr = [0] * (N+1)
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            arr[j] = i

    print(f'#{tc+1}', *arr[1:])
