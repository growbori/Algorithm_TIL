'''
이웃한 두 수의 합이 최대인 경우와 최소인 경우를 찾아 출력하시오
'''

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    sum_two = 0
    sum_list = []
    for i in range(N-1):
        sum_two = numbers[i] + numbers[i+1]
        sum_list.append(sum_two)
        sum_list.sort()
    print(f'#{tc+1} {sum_list[-1]} {sum_list[0]}')
