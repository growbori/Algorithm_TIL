'''
N개의 0과 1로 이루어진 수열에서 연속한 1의 개수중 최댓값을 출력
'''

T = int(input())

for tc in range(T):
    N = int(input())
    numbers = list(input().split('0'))

    max_count = max(numbers)

    print(f'#{tc+1} {max_count.count("1")}')