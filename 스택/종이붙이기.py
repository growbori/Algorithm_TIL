T = int(input())

for tc in range(T):
    N = int(input())

    N = N // 10
    count = [1, 1]

    for i in range(2, N+1):
        count.append(count[i-1] + 2*count[i-2])
    print(f'#{tc+1} {count[-1]}')
