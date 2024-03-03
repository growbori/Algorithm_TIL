N, M = map(int, input().split())
cake = list(map(int, input().split()))

cut = 0
cnt = 0
for i in range(len(cake)):
    if cut == M:
        break
    else:
        if cake[i] == 10:
            cnt += 1
        elif cake[i] >= 10:
            cut += (cake[i] // 10) - 1
            cnt += (cake[i] // 10)
            cake[i] = cake[i] % 10

for i in range(len(cake)):
    if 20> cake[i] >= 10:
        cnt += 1
print(cut, cnt)