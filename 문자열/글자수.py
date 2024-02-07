N= int(input())
for n in range(N):
    str1 = str(input())
    str2 = str(input())
    str_count = 0
    for i in str1:
        max_count = 0
        for j in str2:
            if i == j:
                max_count += 1
        if str_count < max_count:
            str_count = max_count
    print(f'#{n+1} {str_count}')
