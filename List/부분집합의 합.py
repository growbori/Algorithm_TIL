'''
1- 12 까지 숫자를 원소로 가지는 집합A가 있다.
집합 A의 부분집합 중 N 개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 갯수를 출력해라
해당 부분집합이 없는 경우 0을 출력한다.
'''

T = int(input())
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for tc in range(T):
    N, K = map(int, input().split())

    result = 0

    for i in range(1 << len(A)):    # 1<<N : 부분집합의 갯수
        numlist = []

        for j in range(len(A)): # 원소의 수 만큼 비트를 비교
            if i & (1 << j):    # i의 j번 비트가 1인 경우
                numlist.append(A[j])

        if len(numlist)== N and sum(numlist) == K:
            result += 1

    print(result)


