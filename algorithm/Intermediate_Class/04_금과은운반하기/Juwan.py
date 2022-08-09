# 시간 안에 못풀어서 참고해서 품

def solution(a, b, g, s, w, t):
    
    
    upper = (10**14) * 4
    
    lower = 0
    
    answer = (10**14) * 4
    
    while lower <= upper:
        
        mid = (lower+upper) // 2
        gold = 0
        silver = 0
        
        total = 0
        
        for i in range(len(g)):
            
            current_gold = g[i]
            current_silver = s[i]
            current_weight = w[i]
            current_time = t[i]
            
            movement = mid//(current_time*2)
            
            if mid % (current_time*2) >= current_time:
                movement += 1
                
            gold += current_gold if current_gold < movement*current_weight else movement*current_weight
            silver += current_silver if current_silver < movement*current_weight else movement*current_weight
            total += current_gold + current_silver if current_gold + current_silver < movement*current_weight else movement*current_weight
            
        if gold >= a and silver >= b and total >= a+b:
            upper = mid - 1
            answer = min(answer, mid)
        else:
            lower = mid + 1
            
    return answer
