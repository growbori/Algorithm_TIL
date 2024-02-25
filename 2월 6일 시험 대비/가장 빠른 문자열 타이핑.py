T = int(input())
for tc in range(T):
    str1, str2 = map(str, input().split())

    N = len(str1)
    M = len(str2)
    count = str1.count(str2)

    min_count = N-(count*M) + count
    print(min_count)
