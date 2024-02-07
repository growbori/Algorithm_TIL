def push (left):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = left

def pop(): # push 과정
    global top # 제일 위에 있는 item = top
    if top == -1: # 만약 스택이 제일 아랫칸이면
        print('underflow')
        return 0
    else: # 스택이 제일 아랫칸이 아니면
        top -= 1 #위에서부터 한층씩 빼준다.
        stack[top + 1] = 0 # 뺀 나머지 스택에는 0을 표시해준다.
        return 1


T = int(input())
for tc in range(T):

    sentence = input()
    size = len(sentence)
    stack =  [0] * size
    top = -1
    left = '(' or '{'
    right = ')' or '{'


    for i in sentence:
        count = 0
        if i == left:
            push(left)
        elif i == right:
            pop()
# print(stack)

    for j in stack:
        if j != 0:
            answer = 0
        else:
            answer = 1

    print(answer)