T = int(input())
for tc in range(1, T+1):
    word = input()
    stack = []
    for c in word:
        if stack:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        else:
            stack.append(c)
    print(f'#{tc} {len(stack)}')