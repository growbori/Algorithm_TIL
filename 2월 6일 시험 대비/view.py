for tc in range(10):
    N = int(input())
    building = list(map(int, input().split()))
    sum_building = 0
    for i in range(2, N-1):
        if building[i] > building[i+1] and building[i] > building[i+2]:
            if building[i] > building[i-1] and building[i] > building[i-2]:
                sum_building += building[i] - max(building[i-1], building[i-2], building[i+1], building[i+2])

    print(sum_building)