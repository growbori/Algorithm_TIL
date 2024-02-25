T = int(input())
for tc in range(T):
    arr = list(input())

    c = [0] * 12

    for i in arr:
        c[int(i)%10] += 1
    tri = 0
    run = 0
    for i in c:
        if i >= 3:
            c[i] -= 3
            tri += 1

        if i >= 1 and i+1 >= 1 and i+2 >= 1:
            c[i]-= 1
            c[i+1] -= 1
            c[i+2] -= 1
            run += 1

    if tri + run >= 2:
        print('Baby Gin')
    else:
        print('Lose')
