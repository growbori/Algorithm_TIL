T = int(input())

for tc in range(T):
    word = list(input().split())
    N = len(word[0])
    for i in range(N):
        if word[0][i] == word[0][N-1-i]:
            answer = 1
        else:
            answer = 0

    print(f'#{tc+1} {answer}')