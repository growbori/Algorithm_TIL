T = int(input())
for tc in range(T):
    N, M = map(str, input().split())
    arr = list(map(str, input().split()))

    # print(arr)
    new_arr = [0 if x == 'ZRO' else x for x in arr]
    new_arr = [1 if x == 'ONE' else x for x in new_arr]
    new_arr = [2 if x == 'TWO' else x for x in new_arr]
    new_arr = [3 if x == 'THR' else x for x in new_arr]
    new_arr = [4 if x == 'FOR' else x for x in new_arr]
    new_arr = [5 if x == 'FIV' else x for x in new_arr]
    new_arr = [6 if x == 'SIX' else x for x in new_arr]
    new_arr = [7 if x == 'SVN' else x for x in new_arr]
    new_arr = [8 if x == 'EGT' else x for x in new_arr]
    new_arr = [9 if x == 'NIN' else x for x in new_arr]

    new_arr.sort()
    change_arr = ['ZRO' if x == 0 else x for x in new_arr]
    change_arr = ['ONE' if x == 1 else x for x in change_arr]
    change_arr = ['TWO' if x == 2 else x for x in change_arr]
    change_arr = ['THR' if x == 3 else x for x in change_arr]
    change_arr = ['FOR' if x == 4 else x for x in change_arr]
    change_arr = ['FIV' if x == 5 else x for x in change_arr]
    change_arr = ['SIX' if x == 6 else x for x in change_arr]
    change_arr = ['SVN' if x == 7 else x for x in change_arr]
    change_arr = ['EGT' if x == 8 else x for x in change_arr]
    change_arr = ['NIN' if x == 9 else x for x in change_arr]

    print(*change_arr)