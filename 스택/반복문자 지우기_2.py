def push (item): # push 과정
    global top # 제일 위에 있는 item = top
    top += 1 # 하나씩 stack을 쌓아주기
    if top == size: # stack의 높이가 top이랑 같다면
        print('overflow')
    else: # stack의 높이가 top이랑 같지 않다면 item을 쌓아준다.
        stack[top] = item

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
    word = input()
    size = len(word)
    stack = [0] * size # 스택을 쌓을 공간 생성
    top = -1
    count = 0 # for 문 안에서 초기화를 해줘야 누적 합이 나오지 않음!
    for item in word:
        if top == -1: # 맨 아래에 있으면
            push(item) # item을 넣어준다
        else:
            if stack[top] != item: # 만약 맨 위에 있는 요소와 item이 같지 않으면
                push(item) # item을 넣어준다
            else: # 만약 맨 위에 있는 요소와 item이 같으면
                pop() #빼준다
    for i in stack: # 스택 안에 있는 요소들 중
        if i != 0: # 만약 요소가 0 이 아니면
            count += 1 # 카운트를 더해준다

    # print(stack)
    print(f'#{tc+1} {count}')