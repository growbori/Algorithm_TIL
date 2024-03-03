T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    max_count = 0
    count = 0
    for i in arr:

        if i == '1':
            count += 1
        else:
            count = 0
        if max_count < count:
            max_count = count
    print(max_count)