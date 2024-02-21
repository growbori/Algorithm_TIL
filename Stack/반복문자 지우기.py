'''
반복 문자 지우기
stack 활용! stack의 길이가 0일 경우 요소를 하나 더해주고
기존 넣어준 요소와 같은 값이 있을 경우 pop 아닐 경우 append
'''

T = int(input())

for tc in range(T):
    word = list(input())
    stack = []

    for i in word:
        if len(stack) == 0:
            stack.append(i)

        else:
            if i == stack[-1]:
                stack.pop()

            else:
                stack.append(i)

    print(len(stack))