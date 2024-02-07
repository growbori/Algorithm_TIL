T = int(input())
count = 0
for tc in range(T):
    word = list(input())
    N = len(word)
    i = 0
    for i in range(N-1):
        if word[i] == word[i+1]: # for 문을 쓸때마다 N 범위가 줄어들어서 out of range 경고가 뜸
            word.remove(word[i])
            word.remove(word[i+1])
            count += 1
            i = 0
        else:
            i += 1
    print(N - count)




