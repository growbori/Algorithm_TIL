'''
A, B 두 사람에게 교과서에서 찾을 쪽 번호를 알려주면 이진 탐색으로 먼저 펼치는 사람이 이기는 게임이다.
총 400쪽이면, 검색 구간의 왼쪽 l = 1, 오른쪽 r = 400, 중간 페이지 c = int((l+r)/2)
찾는 쪽 번호가 c와 같아지면 탐색을 끝낸다.
책의 전체 쪽수와 두 사람이 찾을 쪽 번호가 주어졌을 때, 이진 탐색 게임에서 이긴 사람을 구하시오.
'''

T = int(input())

for tc in range(T):
    P, Pa, Pb = map(int, input().split())
    cnt = 0
    s1 = 1
    s2 = 1
    P1 = P
    P2 = P
    while True:
        cal1 = int((s1 + P1)/2)
        cal2 = int((s2 + P2)/2)
        if cal1 <= Pa:
            s1 = cal1
        else:
            P1 = cal1
        if cal2 <= Pb:
            s2 = cal2
        else:
            P2 = cal2
        cnt += 1

        if (cal1 == Pa) or (cal2 == Pb):
            break
    if (Pa == cal1) and (Pb == cal2):   # 동점이면
        winner = 0
    elif Pa == cal1:
        winner = 'A'
    elif Pb == cal2:
        winner = 'B'

    print(f'#{tc+1} {winner}')