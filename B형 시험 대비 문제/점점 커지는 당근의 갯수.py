'''
연속으로 당근의 크기가 커진 경우 그 개수를 알려준다
연속으로 커지는 당근의 개수는 최대 얼마인지 확인하는 프로그램을 만드시오
연속으로 커지지 않는 경우 구간의 최소 길이는 1이다.
당근의 크기 C는 1-10
'''

T = int(input())
for tc in range(T):
    N = int(input())
    carrot = list(map(int, input().split()))
    count = 1
    max_count = 1
    for i in range(N-1):
        if carrot[i] < carrot[i+1]:     # 앞의 당근 보다 뒤의 당근 값이 더 크면
            count += 1                  # count에 1을 더해준다.

        else:       # 아니라면
            count = 1   # count 값을 초기화 해준다.

        if max_count < count:   # for 문 안에서 계속 돌면서 count 값과 max_count 값을 비교하며 갱신
            max_count = count

    print(f'#{tc+1} {max_count}')