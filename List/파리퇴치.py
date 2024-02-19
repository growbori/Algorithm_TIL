'''
N * N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미
M * M 크기의 파리채를 한번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 수를 구하라
'''

T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sumlist = []

    for i in range(len(arr)-M+1):
        for j in range(len(arr)-M+1):
            flys = 0
            for x in range(i, i + M):
                for y in range(j, j + M):
                    flys += arr[x][y]
                    sumlist.append(flys)
    sumlist.sort()

    print(sumlist[-1])