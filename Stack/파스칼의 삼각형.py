'''
아래와 같은 규칙으로 파스칼의 삼각형을 만든다.
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
'''

T = int(input())
for tc in range(T):
    N = int(input())

    triangle = [[1] *(i+1) for i in range(N)]

    for x in range(N):
        for y in range(x):
            if y != 0 and x != y:
                triangle[x][y] = triangle[x-1][y-1] + triangle[x-1][y]

    print(f'#{tc+1}')
    for i in range(N):

        print(*triangle[i])
