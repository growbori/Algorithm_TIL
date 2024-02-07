op = {')': '(', '}': '{'}

T = int(input())
for tc in range(1, T + 1):
    s = input()
    ans = 1
    stack = []
    for x in s:
        # if x in '{}()': # 괄호인 경우
        if x in '{(':  # 여는 괄호면 push()
            stack.append((x))  #
        elif x in '})':  # 닫는 괄호면
            if not stack:  # (1) 스택이 비어있으면 오류(break) ans = 0
                ans = 0
                break
            else:  # 스택에 여는괄호가 있으면
                t = stack.pop()
                if t != op[x]:  # (2) pop()해서 짝이 맞지않으면 오류(break) ans = 0
                    ans = 0
                    break
            # (3) 짝이 맞으면 계속
    else:  # 주어진 입력에 대한 확인이 끝난경우
        if stack:  # (4) 스택이 비어있지 않으면(여는 괄호) 오류 ans =0
            ans = 0
    print(f'#{tc} {ans}')