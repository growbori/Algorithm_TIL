'''
두 명의 일꾼에게 수확을 시키려고 한다.
N개의 구역으로 이루어진 당근밭에서 첫 번째 일꾼이 몇 번째 영역까지 수확할 때
두 일꾼이 수확한 당근의 개수 차이가 최소가 되는지 알아내는 프로그램을 만드시오
'''

T = int(input())
for tc in range(T):
    N = int(input())
    carrot = list(map(int, input().split()))
    min_sum = 999999
    k = 0
    for i in range(N-2):
        A = sum(carrot[:i+1])
        B = sum(carrot[i+1:])
        # print(A, B)

        if min_sum > abs(A-B):
            min_sum = abs(A-B)
            k = i       # 수확한 자리의 인덱스 값을 나타냄

    print(f'#{tc+1} {k+1} {min_sum}')     # 당근 수확 첫 지점 인덱스가 0이 아닌 1부터 이므로 k+1