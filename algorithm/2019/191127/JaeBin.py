def solution(begin, target, words):
    answer = 0
    change_list = [begin]

    if target not in words:
        answer = 0
    else:
        while len(words) != 0:
            for item in change_list:
                possible_words = []
                for word in words:
                    check = 0
                    for one in range(len(item)):
                        if item[one] != word[one]:
                            check += 1
                        if check == 2:
                            break
                    if check == 1:
                        possible_words.append(word)
                        words.remove(word)
            answer += 1
            if target in possible_words:
                return answer
            else:
                change_list = possible_words
    return answer