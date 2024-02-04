T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    result = []

    while arr:
        max_number = arr[0]
        min_number = arr[0]

        for number in arr:
            if max_number < number:
                max_number = number

        for number in arr:
            if min_number > number:
                min_number = number

        result.append(max_number)
        result.append(min_number)

        arr.remove(max_number)
        arr.remove(min_number)

    print(f'#{tc+1}', *result[:10], end = '\n')

