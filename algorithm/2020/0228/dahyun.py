

def solution(words):
    answer = 0
    words.sort()
    for idx, word in enumerate(words):
        res = 1
        if idx > 0:
            for i, char in enumerate(word):
                res = max(res, i+1)
                if len(words[idx-1]) == i or words[idx-1][i] != char: 
                    break
        if idx+1 < len(words):
            for i, char in enumerate(word):
                res = max(res, i+1)
                if len(words[idx+1]) == i or words[idx+1][i] != char: 
                    break
        answer += res

    return answer

