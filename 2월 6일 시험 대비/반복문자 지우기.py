T = int(input())
for tc in range(T):
    arr = list(input())
    stack = []
    top = -1
    # print(arr)
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    print(len(stack))