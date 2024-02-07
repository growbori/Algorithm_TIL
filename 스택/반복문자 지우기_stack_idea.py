'''
stack top 원소(peak)

'''

def stack(item, size):
    global top
    top += 1
    if N == isEmpty: # stack이 비어있으면 채워주기
        N.append(item)

    elif top == size: # 제일 상단의 스택이랑 새로 넣으려는 stack이 같으면
        N.pop(top) # 둘다 제거해주기
        N.pop(item)

    else: # 제일 상단의 스택이랑 새로 넣으려는 스택이 다르면
        stack[top] = item



T = int(input())
for tc in range(T):
    case = list(input())

for i in range(len(case)):
    item = case[i]
    size = case[i+1]
N = []

stack(item, size)
