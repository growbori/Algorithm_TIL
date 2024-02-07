def pascal(N):
    nums = [0]* N
    nums[0], nums[-1] = 1, 1 # 처음 자리와 마지막 자리는 무조건 1
    if N > 2:
        prepascal = pascal(N-1)
        for i in range(1, N-1):
            nums[i] = prepascal[i-1] + prepascal[i]
    return nums


T = int(input())
for tc in range(T):
    N = int(input())
    print(f'#{tc+1}')
    for i in range(1, N+1):
        print(*pascal(i))