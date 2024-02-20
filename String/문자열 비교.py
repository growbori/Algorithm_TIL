'''
str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램
첫 문자열이 두번째에 존재하면 1 존재하지 않으면 0을 출력
'''

T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()

    if str1 in str2:
        answer = 1

    else:
        answer = 0

    print(answer)