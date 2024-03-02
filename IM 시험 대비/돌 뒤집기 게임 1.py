T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    for x in range(M):
        i, j = map(int, input().split())

        for k in range(1, j+1):
            if 0 <= i+k <= N:
                if arr[i] == 1:
                    arr[i+k] = 1
                elif arr[i] == 0:
                    arr[i+k] = 0

    print(f'#{tc+1}', *arr[1:])