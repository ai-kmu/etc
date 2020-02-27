def solution(words):
    words.sort()
    answer = 0

    for word in range(len(words) - 1):
        count_front = 0
        count_rear = 0

        min_word_length = min(len(words[word]), len(words[word+1]))
        for char in range(min_word_length):
            if words[word][char] != words[word + 1][char]:
                count_front += 1
                break
            else:
                count_front += 1


        min_word_length = min(len(words[word]), len(words[word-1]))
        for char in range(min_word_length):
            if words[word][char] != words[word-1][char]:
                count_rear += 1
                break
            else:
                count_rear += 1
        if len(words[word]) > min_word_length:
            count_rear += 1

        answer += max(count_front, count_rear)

    count_front = 0
    min_word_length = min(len(words[-1]), len(words[-2]))
    for word in range(min_word_length):
        if words[-1][word] != words[-2][word]:
            break
        else:
            count_front += 1
    if len(words[-1]) > min_word_length:
        count_front += 1

    answer += count_front

    return answer

words_1 = ['go', 'gone', 'guild']
words_2 = ['abc', 'def', 'ghi', 'jklm']
words_3 = ['word', 'war', 'warrior', 'world']
print(solution(words_1))
print()
print(solution(words_2))
print()
print(solution(words_3))