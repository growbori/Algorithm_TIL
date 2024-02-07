def push (item):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = item

def pop(): # push 과정
    global top # 제일 위에 있는 item = top
    if top == -1: # 만약 스택이 제일 아랫칸이면
        # print('underflow')
        return 0
    else: # 스택이 제일 아랫칸이 아니면
        top -= 1 #위에서부터 한층씩 빼준다.
        #stack[top + 1] = 0 # 뺀 나머지 스택에는 0을 표시해준다.
        return stack[top+1] # 기존에 들어있는 얘를 리턴해주면 됨


T = int(input())
for tc in range(T):

    sentence = input()
    size = len(sentence)
    stack = [0] * size
    top = -1
    left1 = '('
    left2 = '{'
    right1 = ')'
    right2 = '}'
    answer = 1
    for i in sentence:
        count = 0
        if i == left1:
            push(left1)
        elif i == left2:
            push(left2)
        elif i == right1: # 닫는 괄호
            t = pop()
            if t == 0 or t!=left1:
                answer = 0
                break
        elif i == right2:
            t = pop()
            if t == 0 or t != left2:
                answer = 0
                break
    # print(stack)

    if top != -1: # 스택에 여는 괄호가 남아있으면
        answer = 0

    print(f'#{tc+1} {answer}')