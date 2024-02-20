'''
N 길이의 숫자열을 오름차순으로 정렬하여 출력
'''

T = int(input())

for tc in range(T):
    N = int(input())

    arr = list(map(int, input().split()))

    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                arr[min_idx], arr[j] = arr[j], arr[min_idx]

    print(arr)