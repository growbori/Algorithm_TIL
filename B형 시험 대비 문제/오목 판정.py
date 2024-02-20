'''
N * N 크기의 판 가로, 세로 대각선 중 하나의 방향으로 다섯개 이상 연속
'''


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    omok = 0

    for i in range(N):
        vertical = ''
        horizon = ''
        for j in range(N):
            vertical += arr[i][j]
            if 'ooooo' in vertical:
                omok += 1

            horizon += arr[j][i]
            if 'ooooo' in horizon:
                omok += 1


    for i in range(N-5+1):
        for j in range(N-5+1):
            diagonal = ''
            diagonal_reverse = ''
            for x in range(5):
                for y in range(5):
                    if x == y:
                        diagonal += arr[i + x][j + y]
                        if 'ooooo' in diagonal:
                            omok += 1
                    if x + y == 4:      # 	(0, 4) (1, 3) (2, 2) (3, 1) (4, 0) 일때 역대각선이 성립
                        diagonal_reverse += arr[i + x][j + y]
                        if 'ooooo' in diagonal_reverse:
                            omok += 1

    if omok >= 1:
        answer = 'YES'
    else:
        answer = 'NO'

    print(f'#{tc+1} {answer}')


'''
예상 오류 케이스
x o x  x x
x x o x x x
x x x o x x
x x x x o x
x x x x x o
x x x x x x 
'''