N = int(input())
arr = [int(input()) for _ in range(N)]
print(arr)
count = 0
for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            count += 1
print(arr)
print(count)