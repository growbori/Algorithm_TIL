T = int(input())
for tc in range(T):
    N = int(input())
    card = list(input())

    c = [0] * 10

    for i in card:
        c[int(i)%10] += 1

    max_idx = 0
    max_num = 0
    for i in range(1, len(c)):
        if c[max_idx] <= c[i]:
            max_idx = i
            max_num = c[i]

    print(max_idx, max_num)