T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()
    # print(arr)
    new_arr = []
    while arr:
        a = arr.pop()
        b = arr.pop(0)

        new_arr.append(a)
        new_arr.append(b)


    print(*new_arr)