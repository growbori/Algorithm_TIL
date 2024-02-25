for tc in range(10):
    dump = int(input())
    yellow_box = list(map(int, input().split()))

    for _ in range(dump):
        max_box, min_box = 0, 101
        max_idx, min_idx = 0, 0

        for i in range(len(yellow_box)):
            if min_box > yellow_box[i]:
                min_box = yellow_box[i]
                min_idx = i

            if max_box < yellow_box[i]:
                max_box = yellow_box[i]
                max_idx = i

        yellow_box[max_idx] -= 1
        yellow_box[min_idx] += 1

    max_h = 0
    min_h = 0

    for box in yellow_box:
        if max_h < box:
            max_h = box
        if min_h > box:
            min_h = box

    print(max_h - min_h)