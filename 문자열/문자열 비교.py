N = int(input())

for n in range(N):
    str1 = input()
    str2 = input()

    if str1 in str2:
        answer = 1
    else:
        answer = 0

    print(f'#{n+1} {answer}')