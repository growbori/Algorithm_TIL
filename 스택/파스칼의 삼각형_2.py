arr = [[0]*(i+1) for i in range(4)]

T = int(input())

for tc in range(T):
    n = int(input())
    for i in range(0, n+1):
        for j in range(0, i):
            if j == 0 or i == j:
                arr[i][j] = 1

            else:
                arr[i][j] = arr[i-1][j-1]+ arr[i-1, j]

print(arr)