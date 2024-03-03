# 밀어서 덮어씌운다.
T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    arr = arr[1:]
    count = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                count += 1
    # print(arr)
    print(f'{tc+1} {count}')

