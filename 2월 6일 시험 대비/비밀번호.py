for tc in range(10):
    N, arr = input().split()
    stack = []
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    print(''.join(stack))