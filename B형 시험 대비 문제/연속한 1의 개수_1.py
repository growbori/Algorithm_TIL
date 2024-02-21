T = int(input())

for tc in range(T):
    N = int(input())
    num_list = str(input())
    max_count = 0
    count = 0

    for i in num_list:
        if i == '1':
            count += 1

        else:
            count=0

        if max_count < count:
            max_count = count

    print(f'#{tc+1} {max_count}')