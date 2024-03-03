'''
난쟁이가 일곱이 아닌 아홉명이었다!
다행히 일곱 난쟁이 키의 합이 100이 됨을 기억해냈다.
난쟁이의 키의 합은 모두 다르며 가능한 답이 여러개인 경우에는 아무거나 출력한다.
난쟁이의 키를 오름차순으로 출력한다.
'''



height = [int(input()) for _ in range(9)]

for i in range(9):
    for j in range(i+1, 9):
        for k in range(j+1, 9):
            for x in range(k+1, 9):
                for y in range(x+1, 9):
                    for w in range(y+1, 9):
                        for q in range(w+1, 9):
                            if height[i] + height[j] + height[k] + height[x] + height[y] + height[w] + height[q] == 100:
                                answer = [height[i], height[j], height[k], height[x], height[y], height[w], height[q]]
answer.sort()

for h in answer:
    print(h, end = '\n')
