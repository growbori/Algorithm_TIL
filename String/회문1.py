'''
8*8 평면 글자판에서 제시된 길이를 가진 회문의 개수를 구하여라
'''



for tc in range(10):
    N = int(input())
    word = [input() for _ in range(8)]
    count = 0
    #가로 탐색

    for i in range(8):
        for j in range(8-N+1):
            if word[i][j:j+N] == word[i][j:j+N][::-1]:
                count += 1

    for i in range(8-N+1):
        for j in range(8):
            vertical = ''
            for x in range(i, i+N):
                vertical += word[x][j]
            if vertical == vertical[::-1]:
                count += 1
    print(count)