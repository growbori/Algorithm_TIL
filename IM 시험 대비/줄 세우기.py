N = int(input())
arr = list(map(int, input().split()))

a_list = [n for n in range(1, N+1)]
for i in range(N):  # i 위치의 학생을 순서대로 이동을 처리
    n, t = arr[i], a_list[i]    # 앞으로 이동할 칸 수, 학생 번호
    for j in range(i, i-n, -1):
        a_list[j] = a_list[j-1]
    a_list[i-n] = t

print(*a_list)