def palin(n, m, block):
    ansRow = 0
    startIdx = 0
    endIdx = 0
 
    for i in range(n):
        for a in range(n - m + 1): 
            cnt = 0
            for b in range(m // 2): 
 
                if block[i][a + b] == block[i][(m + a) - 1 - b]: 
                    cnt += 1
 
            if cnt == m // 2:  
                ansRow = i 
                startIdx = a
                endIdx = m + a
 
    ans = []
    if ansRow != 0:
        for word in range(startIdx, endIdx):
            ans.append(block[ansRow][word])
    return ans
 
 
T = int(input())
for tc in range(1, T + 1):
    lenarr, lenpat = map(int, input().split())
    blockR = [list(str(input())) for _ in range(lenarr)]
 
    # 가로 함수값
    ansRow = palin(lenarr, lenpat, blockR)
 
    # 세로
    # 2차원 배열 초기화
    blockC = [[0] * lenarr for _ in range(lenarr)]
 
    for x in range(lenarr):
        for y in range(lenarr):
            blockC[x][y] = blockR[y][x]
 
    # 세로 함수값
    ansCol = palin(lenarr, lenpat, blockC)
 
    if ansRow:
        print(f'#{tc}', end=" ")
        for letter in range(len(ansRow)):
            print(ansRow[letter], end="")  # 1 TLMMHOOOHMMLT
        print()
    else:
        print(f'#{tc}', end=" ")
        for letter in range(len(ansCol)):
            print(ansCol[letter], end="")
        print()