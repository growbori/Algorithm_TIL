def push(item):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = item

def pop():
    global top
    if top == -1:
        return 0
    else:
        top -= 1
        stack[top +1] = 0
        return 1


for tc in range(10):
    N, number = map(int, input().split())
    size = len(str(number))
    stack = [0] * size
    top = -1
    for item in str(number):
        if top == -1:
            push(item)
        else:
            if stack[top] != item:
                push(item)
            else:
                pop()
    answer = []
    for i in stack:
        if i != 0:
            answer.append(i)

    # print(answer)
    new_answer = ''.join(answer)

    print(f'#{tc+1} {(new_answer)}')

