'''
각 색종이가 보이는 부분의 면적을 구하는 프로그램을 작성하시오
전체를 돌리면 런타임이 오래 걸릴 것임
'''

N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
for n in range(1, N+1):
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        # 리스트 단위로 표시
        arr[i][sj:sj+w] = [n] * w
        # for j in range(sj, sj+w):
        #     arr[i][j] = n
#
# for n in range(1, N+1):
#     count = 0
#     for lst in arr:
#         count += lst.count(n)
#     print(count)

'''
빈도수 배열을 사용해서 ,arr 한번만 순회
'''
cnt = [0] * (N+1)
for lst in arr:
    for n in lst:
        cnt[n] += 1

print(*cnt[1:], end = '\n')
