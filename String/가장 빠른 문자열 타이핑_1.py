'''
A를 타이핑 하려고 하는데 B문자열이 저장되어 있어 키를 한번 누르는 것으로 B전체를 타이핑 할 수 있다.
전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의
'''

T = int(input())
for tc in range(T):
    str1, str2 = map(str, input().split())
    N = len(str1)
    M = len(str2)
    count = str1.count(str2)
    result = N - M * count + count
    print(result)