'''
N개의 정수 중 짝수의 갯수를 출력하시오
'''

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    answer = 0
    for i in numbers:
        if i % 2 == 0:
            answer += 1

    print(f'#{tc+1} {answer}')