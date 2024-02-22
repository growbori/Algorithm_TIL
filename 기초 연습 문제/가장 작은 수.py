'''
N개의 정수 중 가장 작은 수는 몇 번째 숫자인지 출력하시오
단 첫번째 위치는 1부터 시작한다.
'''

T = int(input())
for tc in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))

    min_idx = 0

    for i in range(1, N):

        if numbers[min_idx] > numbers[i]:
            min_idx = i

    print(f'#{tc+1} {min_idx+1}')