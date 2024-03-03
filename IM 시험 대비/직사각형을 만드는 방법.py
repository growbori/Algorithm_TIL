N = int(input())
arr = [1, 2]

for i in range(2, N-1):
    A = arr[i-1] + arr[i-2]
    arr.append(A)
    i += 1
    answer = arr[-1]
print(answer)