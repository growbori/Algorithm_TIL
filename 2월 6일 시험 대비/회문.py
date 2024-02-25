T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                answer = arr[i][j:j+M]
                answer = ''.join(answer)

    for i in range(N-M+1):
        for j in range(N):
            vertical = ''
            for x in range(i, i+M):
                vertical += arr[x][j]
            if vertical == vertical[::-1]:
                answer = vertical

    print(f'#{tc+1} {answer}')