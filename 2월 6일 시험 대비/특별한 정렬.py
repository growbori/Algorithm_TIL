T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    new_arr = []
    arr.sort()
    while arr:
        a = arr.pop()
        b = arr.pop(0)

        new_arr.append(a)
        new_arr.append(b)

    print(*new_arr[:10])

