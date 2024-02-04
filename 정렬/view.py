for j in range(10):
    n = int(input())
    array = list(map(int, input().split()))

    height = 0
    for i in range(2, n-2):
        if array[i] > array[i+1] and array[i] > array[i+2]:
            if array[i] > array[i-1] and array[i] > array[i-2]:
                height += (array[i] - max(array[i-1], array[i-2], array[i+1], array[i+2]))


    print(f'#{j+1} {height}')
