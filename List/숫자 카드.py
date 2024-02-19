'''
0에서 9까지 적힌 숫자 N장
가장 많은 카드에 적힌 숫자와 카드가 몇장인지 출력
카드 장수가 같을 땐 적힌 숫자가 큰 쪽을 출력
'''

T = int(input())
for tc in range(T):
    N = int(input())
    arr = input()
    card = [0] * 10

    for x in arr:
        card[int(x) % 10] +=1
    max_idx = 0
    for i in range(len(card)):
        if card[max_idx] <= card[i]:
            max_idx = i



    print(max_idx,  max(card))