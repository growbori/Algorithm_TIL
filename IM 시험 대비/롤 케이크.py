'''
첫째 줄에는 가장 많은 조각을 받을것으로 기대하고 있던 방청객 번호
둘째 줄에는 가장 많은 조각을 받은 방청객 번호
'''

L = int(input())
N = int(input())
list = [0] * (L+1)
list2 = [0] * (L+1)
for n in range(N):
    P, K = map(int, input().split())

    max_diff

max_count = 0
idx = 0
for i in range(1, n+1):
    cnt = list2.count(i)
    if max_count < cnt:
        max_count = cnt
        idx = i

print(idx)
