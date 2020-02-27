def solution(words):
    word_dict = build_dict(words)
    total_num = 0
    for word in words:
        for i in range(len(word)):
            if len(word_dict[word[:i+1]]) == 1:
                total_num += i + 1
                break
        else:
            total_num += len(word)
            
    return total_num

def build_dict(words):
    d = {}
    for word in words:
        for i in range(len(word)):
            if not d.get(word[:i+1]):
                d[word[:i+1]] = [word]
            else:
                d[word[:i+1]].append(word)
    return d
