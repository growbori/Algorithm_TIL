'''
N * N 크기의 판 가로, 세로 대각선 중 하나의 방향으로 다섯개 이상 연속
'''


T = int(input())

for tc in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    omok = 0

    for i in range(N):
        for j in range(N):
            vertical = ''
            for x in range(5):
                vertical += arr[x][j]
                if vertical == 'ooooo':
                    omok += 1
            horizon = ''
            for y in range(5):
                horizon += arr[i][y]
                if horizon == 'ooooo':
                    omok += 1

            diagonal = ''
            diagonal += arr[i][i]
            if diagonal == 'ooooo':
                omok += 1

            diagonal_reverse = ''
            for z in range(5):
                diagonal_reverse += arr[j][j]
                if diagonal_reverse == 'ooooo':
                    omok += 1
    if omok >= 1:
        answer = 'YES'
    else:
        answer = 'NO'


    print(f'#{tc+1} {answer}')