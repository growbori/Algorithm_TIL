'''
N 개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오
'''

T = int(input())

for tc in range(T):
    N = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    diff = arr[-1] - arr[0]

    print(f'#{tc+1} {diff}')