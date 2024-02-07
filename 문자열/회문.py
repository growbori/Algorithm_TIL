T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    # 가로 탐색
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j: j + M] == arr[i][j: j + M][::-1]:
                answer = arr[i][j : j+ M]

    # 세로 탐색

    for i in range(N-M+1): # 가로로 적힌 값
        for j in range(N): # 세로로 적힌 값
            vertical = '' # vertical이라는 단어를 생성
            for x in range(i, i+M): # x 가 M 까지의 단어 길이 사이에 있을 때
                vertical += arr[x][j]
            if vertical == vertical[::-1]: # vertical과 vertical 뒤집은 단어가 같으면
                answer = vertical

    print(f'#{tc} {answer}')

