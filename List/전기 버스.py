'''
0-N 정류장 이동하고 한번 충전으로 최대 K정류장 만큼 이동 가능하다.
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력해라
충전기가 잘못 설치되어 종점에 도착할 수 없는 경우 0을 출력한다.
'''

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charger = [0] + list(map(int, input().split())) + [N]

    last = 0
    count = 0
    for i in range(1, M+2):
        if (charger[i] - charger[i-1]) <= K:    # 충전기 사이에서는 운행 가능
            if (charger[i] - last) > K: #마지막 충전기에서 너무 멀면
                last = charger[i-1]
                count += 1
            
            else:
                count = 0
                break
    print({count})