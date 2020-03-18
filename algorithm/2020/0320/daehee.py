def solution(priorities, location):
    answer = 1
    try:
        while True:

            now = priorities[0]
            del priorities[0]
            location -= 1

            if now >= max(priorities):
                if location < 0:
                    break
                answer += 1
            else:
                if location < 0:
                    location = len(priorities)
                priorities.append(now)    
        
    except:
        return answer
    
    return answer
