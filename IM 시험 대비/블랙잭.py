'''
카드의 합이 21을 넘지 않는 한도 내에서 카드의 합을 최대한 크게 만드는 게임
N 장의 카드를 숫자가 보이게 내려놓고 M을 크게 외친다.
제한된 시간 안에 N장의 카드 중 3장을 골ㄴ다.
고른 합은 M이 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
'''

N, M = map(int, input().split())
arr = list(map(int, input().split()))
max_sum = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i] + arr[j] + arr[k] <= M:
                answer = arr[i] + arr[j] + arr[k]

                if max_sum < answer:
                    max_sum = answer
print(max_sum)