T = int(input())

for _ in range(T):
    tc, N = input().split()
    arr = input().split()
    count = [0] * 10
    language = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for i in arr:
        for j in range(10):
            if i == language[j]:
                count[j] += 1
                break
    print(tc)
    for i in range(10):
        print(f'{language[i]} '* count[i], end = ' ')   # {language} 다음 띄어쓰기 유의하기
    print()