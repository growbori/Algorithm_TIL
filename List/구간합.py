'''
N개의 정수가 들어있는 배열에서 이웃한 M개의 합을 구하기
M 개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력
'''


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sumlist = []
    for i in range(N-M+1):
        summ = 0
        for j in range(i, i + M):
            summ += arr[j]
        sumlist.append(summ)
    sumlist.sort()
    print(f'#{tc+1} {sumlist[-1] - sumlist[0]}')

