def isChangable(s1, s2):
    count = 0 
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            count +=1 

    return len(s1) - 1 == count 

def findTarget(begin, target, words):


    if isChangable(begin, target):
        if target in words:
            return 1

    result = []

    for w in words:
        if isChangable(begin, w):
            words.remove(w)
            result.append(1+findTarget(w, target, words))

    if not result:
        return 0
    else:
        return min(result)

def solution(begin, target, words):
    answer = 0
    if target in words:
        answer = findTarget(begin, target, words)
    return answer
