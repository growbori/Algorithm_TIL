t = int(input())
 
for test_case in range(1, t + 1):
    word, short_word = map(str, input().split())
    length_word = len(word)
    length_short_word = len(short_word)
    short_word_count = 0
    word_index = 0
 
    while word_index < length_word:
        if word[word_index:word_index + length_short_word] == short_word: # 길이를 항상 유지하기 위해 word_index : word_index 사용!
            short_word_count += 1
            word_index += length_short_word
        else:
            word_index += 1
 
    result = length_word - (length_short_word - 1) * short_word_count
 
    print(f'#{test_case} {result}')