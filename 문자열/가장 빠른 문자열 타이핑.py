T = int(input())

for tc in range(T):
    A, B = input().split()
    N = len(A)
    M = len(B)
    count = A.count(B)
    Min_count = N-(count*M)+count
    print(f'#{tc+1} {Min_count}')

