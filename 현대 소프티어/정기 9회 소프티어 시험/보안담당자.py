N = int(input())
CCTV = input()
stack = []
for i in range(len(CCTV)):
    if len(stack) == 0:
        stack.append(CCTV[i])
    else:
        if stack[-1] == '(' and CCTV[i] == ')' or CCTV[i] == '?':
            stack.pop()
        elif stack[-1] == '?' and CCTV[i] == ')':
            stack.pop()
        elif stack[-1] == '?' and CCTV[i] == '?':
            stack.pop()
        else:
            stack.append()

if len(stack) == 0:
    print('Yes')
else:
    print('No')