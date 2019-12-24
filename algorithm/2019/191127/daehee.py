def check(sample, gt):
    number = 0
    for idx, letter in enumerate(list(sample)):
        if letter != gt[idx]:
            number += 1
        if number > 1:
            return False
    return True

def dfs(depth,words, now , target, costs):
    if now == target:
        costs.append(depth)
        return
    
    avails = words
    for word in words:
        c = check(word, now)
        if c == True:
            avails.remove(word)
            d = dfs(depth+1, avails, word, target, costs)
            avails.append(word)
            
    return 0
        
def solution(begin, target, words):
    costs = list()
    dfs(0, words, begin, target, costs)
    answer = 0
    if costs:
        answer = min(costs)
    
    return answer