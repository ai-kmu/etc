def solution(words):
    answer = 0
    words.sort()
    
    
    for idx in [0, len(words)-1]:
        cases = -1 if idx > 0 else 1
        for order in range(len(words[idx])):
            try:
                if words[idx][order] == words[idx+cases][order]:
                    answer += 1
                else:
                    answer += 1
                    break
            except:
                answer += 1
                break
                
    
    for idx in range(1,len(words)-1):
        left = 0
        right = 0
        for order in range(len(words[idx])):
            try:
                if words[idx-1][order] == words[idx][order]:
                    left += 1
                else:
                    left += 1
                    break
            except:
                left += 1  
                break
        for order in range(len(words[idx])):
            try:
                if words[idx][order] == words[idx+1][order]:
                    right += 1
                else:
                    right += 1
                    break
            except:
                right += 1  
                break
        answer += max(left,right)
    return answer
