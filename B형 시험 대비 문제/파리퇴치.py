'''
N*N 배열 안에 파리가 존재!
M*M 크기의 파리채를 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 최대 수를 구하여라
'''

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    fly_list = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            count = 0
            for x in range(M):
                for y in range(M):
                    count += fly_list[i + x][j + y]

            if max_count < count:
                max_count = count

    print(max_count)