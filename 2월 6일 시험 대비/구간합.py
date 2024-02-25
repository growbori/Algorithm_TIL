T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    sum_list = []
    for i in range(N-M+1):
        summ = 0
        for k in range(i, i+M):
            summ += arr[k]
        sum_list.append(summ)
    sum_list.sort()
    print(sum_list[-1] - sum_list[0])
