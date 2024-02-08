'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(i, V): # 시작 i, 마지막 V
    visited = [0] * (V+1) # visited, stack 생성 및 초기화
    stack = []
    visited[i] = 1  # 시작점 방문
    print(i)        # 정점에서 할 일
    while True:     # 탐색
        for w in adjl[i] :# 현재 방문한 정점에 인접하고 방문안한 정점w가 있으면
            if visited[w] == 0 : # 만약 방문한 적이 없으면
                stack.append(i) # push(i), i를 지나서
                i = w # w에 방문
                visited[i] = 1 # 방문해서 할일(1표시)
                print(i)
                break # for w
        else:                   # for w, i에 남은 인접 정점이 없으면
            if stack:   # 스택이 비어있지 않으면(지나온 정점이 남아있으면)
                i = stack.pop()
            else:
                break   # while True
    return

V, E = map(int, input().split()) # V 1~7 까지 숫자, E 노드의 수
arr =list(map(int, input().split())) # 2개씩 연결된 노드들을 전부 나열한 것

# 인접리스트
adjl = [[] for _ in range(V+1)] # ardjl[i] 행에 i에 인접인 정점번호

for i in range(E):
    n1, n2 = arr[i * 2] , arr[i * 2 + 1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) # 방향이 없는 경우 방향이 있는 경우에는 넣으면 안됨

# print(adjl)
'''
[[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]
0번에 인접한 숫자, 1번에 인접한 숫자, 2번에 인접한 숫자...
'''
dfs(1, V) # 1번부터 탐색하고 마지막 정점 번호는 V
