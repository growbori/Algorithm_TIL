for tc in range(1, 11):
    N, nums = input().split()
    stack = []
    for i in range(int(N)):
        if stack:
            if stack[-1] == nums[i]:
                stack.pop()
            else:
                stack.append(nums[i])
        else:
            stack.append(nums[i])
    print(f"#{tc} {''.join(stack)}")