'''
str1에 포함된 글자들이 str2에 몇개씩 있는지 찾고, 그중 가장 만은 글자의 개수를 출력
'''

T = int(input())
for tc in range(T):
    str1 = list(input())
    str2 = list(input())
    same = []
    for x in str1:
        if x in str2:
            same.append(x)
    max_alpha = max(same)
    count = 0
    cnt= str2.count(max_alpha)

    print(cnt)