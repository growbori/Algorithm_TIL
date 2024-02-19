'''
1-9로 구성된 6개의 숫자를 읽어 베이비진을 판단하는 프로그램을 만드시오
'''

T = int(input())

for tc in range(T):
    arr = input()
    number = [0] * 12

    for x in arr:
        number[int(x) % 10] += 1
    i = 0
    # print(number)
    tri = run = 0

    while i < 10:
        if number[i] >= 3:
            number[i] -= 3
            tri += 1
            continue
        if number[i] == 1 and number[i+1] == 1 and number[i+2] == 1:
            number[i]-= 1
            number[i-1] -= 1
            number[i-2] -= 1
            run += 1
            continue
        i += 1

    if tri + run == 2:
        print('Baby Gin')
    else:
        print('Lose')


