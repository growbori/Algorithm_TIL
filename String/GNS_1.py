'''
"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"

0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램

'''

T = int(input())

for tc in range(T):
    str = input()
    arr = input().split()
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
    # print(new_arr)
    change_arr = ['ZRO' if x == 0 else x for x in new_arr]
    change_arr = ['ONE' if x == 0 else x for x in change_arr]
    change_arr = ['TWO' if x == 0 else x for x in change_arr]
    change_arr = ['THR' if x == 0 else x for x in change_arr]
    change_arr = ['FOR' if x == 0 else x for x in change_arr]
    change_arr = ['FIV' if x == 0 else x for x in change_arr]
    change_arr = ['SIX' if x == 0 else x for x in change_arr]
    change_arr = ['SVN' if x == 0 else x for x in change_arr]
    change_arr = ['EGT' if x == 0 else x for x in change_arr]
    change_arr = ['NIN' if x == 0 else x for x in change_arr]

    print(*change_arr)