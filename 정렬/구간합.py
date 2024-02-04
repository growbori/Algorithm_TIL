N = int(input())

for n in range(N):
    a, b = map(int, input().split())
    array = list(map(int, input().split()))
    sum_array = []
    for i in range(a-b+1):
        summ = 0
        for j in range(i, i+ b):
            summ += array[j]
        sum_array.append(summ)

    sum_array.sort()
    result = sum_array[-1] - sum_array[0]
    print(f'#{n+1} {result}')