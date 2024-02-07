T = int(input())

for tc in range(T):
    n = int(input())
    arr = [[1] * (i + 1) for i in range(n)]
    for i in range(0, n):
        for j in range(0, i):

            if j != 0 and i != j:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

print(f'#{tc+1}')
for i in range(1, n):
    print(*arr[i])
