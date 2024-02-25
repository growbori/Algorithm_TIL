T = int(input())
for tc in range(T):
    word = list(input())
    # print(word)
    for i in range(len(word)):
        if word == word[::-1]:
            answer = 1
        else:
            answer = 0

    print(answer)