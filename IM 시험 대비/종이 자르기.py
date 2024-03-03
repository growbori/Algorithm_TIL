'''
가로 0 세로 1 자르기
시작점부터 차이가 가장 큰 놈을 찾기!
반드시 오름차순으로 들어오지 않을 수도 있음 (sort 필요)
그 길이 중 가장 긴 길이 찾기
'''

C, R = map(int, input().split())
# 1. 가로/세로 자르는 위치를 저장 후 정렬
r_list = [0, R]
c_list = [0, C]
N = int(input())
for _ in range(N):
    t, n = map(int, input().split())
    if t == 0:
        r_list.append(n)
    else:
        c_list.append(n)

r_list.sort()
c_list.sort()

# 2. 가장 긴 길이 찾기
r_max = 0
for i in range(1, len(r_list)):
    r_max = max(r_max, r_list[i] -r_list[i-1])

c_max = 0
for i in range(1, len(c_list)):
    c_max = max(c_max, c_list[i] - c_list[i-1])

answer = r_max * c_max

print(answer)

