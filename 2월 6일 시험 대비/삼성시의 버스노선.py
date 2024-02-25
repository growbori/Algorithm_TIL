T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노선수
    bus_box = [0] + [0] * 5000  #1-5000번까지 노선 수

    for i in range(N):
        A, B = map(int, input().split())

        for j in range(A, B+1):
            bus_box[j] += 1
    P = int(input())    # 출력할 정류장 수
    print(f'#{tc}', end=' ')
    for _ in range(P):  # P번 반복
        num = int(input())  # 노선수를 출력할 정류장 번호
        print(bus_box[num], end = ' ')

    print() # 다 적고 줄을 바꿔줘!

