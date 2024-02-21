'''
10*10 격자에 빨간색과 파란색을 칠하고자 한다.
칠이 끝난 후 빨간색 영역과 파란색 영역의 외곽 길이를 구하는 프로그램을 구하시오
=> 두 사각형 외곽의 길이 합을 구하면 됨
'''

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total_length = 0
    for i in range(N):
        c1, a1, c2, a2, color = arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4]

        total_length += (2*(c2-c1+1) + 2* (a2-a1+1))


    print(f'#{tc+1} {total_length}')

'''
발생할 수 있는 예외 상황 (테스트 케이스 10 중 8 맞음)
빨간 혹은 파란색 네모 안에 다른 네모가 들어있을 경우
'''