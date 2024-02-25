T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = [0]+ list(map(int, input().split())) + [N]

    last = 0
    count = 0

    for i in range(1, M+2): # 모든 충전기 갯수에 대해
        if (charger[i] - charger[i-1]) <= K:    #충전기 사이에 운행 가능하면
            if (charger[i] - last) > K:     # 마지막 충전기에서 너무 멀면
                last = charger[i-1]
                count += 1
        else:
            count = 0
            break

    print(f'#{tc} {count}')


