'''
숫자 1은 0, 0은 1로 바뀌는 연산을 토글이라 한다.
각 칸이 1또는 0으로 초기화 된 N*N 영역이 주어진다.
M 초까지 1초마다 다음 조건으로 토글된다.
k초가 되는 순간 i+j가 k와 같거나 k의 배수가 되는 영역을 토글이라 한다.
M이 k의 배수인 경우와 M초에는 전체가 토글됨
'''

'''
if (i+j) % k == 0  or (i+j) == k 토글
M초후 1인 영역의 갯수 count 
'''
T = int(input())

for tc in range(T):
    N, M = map(int, input().split())    # M초마다 변화
    arr = [list(map(int, input().split())) for _ in range(N)]   # 시작

    for k in range(1, M+1):
        for i in range(N):
            for j in range(N):
                if (i+j+2) % k == 0 or (i+j+2) == k:
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    elif arr[i][j] == 1:
                        arr[i][j] = 0
                elif M % k == 0:    # M인 경우에는 전체가 토글된다.
                    if arr[i][j] == 0:
                        arr[i][j] = 1
                    elif arr[i][j] == 1:
                        arr[i][j] = 0
    count = 0
    for i in arr:
        for j in i:
            if j == 1:
                count += 1
    # print(arr)
    print(f'#{tc+1} {count}')