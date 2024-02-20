'''
단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력
'''

T = int(input())
for tc in range(T):
    txt = list(map(str, input()))
    # print(txt)
    # print(txt[::-1])
    if txt == txt[::-1]:
        answer = 1
    else:
        answer = 0
    print(answer)