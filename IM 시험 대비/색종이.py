'''
가로, 세로의 크기가 100인 정사각형 모양의 흰색 도화지가 있다.
가로 세로 크기가 각각 10인 정사각형 모양의 검은색 종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.
색종이를 한장 또는 여러장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하시오
전체 넓이를 구하고 겹치는 부분의 넓이 빼기
'''


N = int(input())
board = [[0] * 100 for _ in range(100)]
for _ in range(N):

    A, B = map(int,input().split())
    for x in range(A, A + 10):
        for y in range(B, B + 10):
            board[x][y] += 1

total = 0
for i in range(100):
    for j in range(100):
        if board[i][j] >= 1:
            total += 1


print(total)
