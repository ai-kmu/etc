def solution(A, B):
    answer = 0
    if min(A) >= max(B):
        return answer
    else:
        B.sort()
        for a in A:
            win_b = B[-1]
            if a >= win_b:
                B.pop(0)
            else :
                for b in B:
                    if b > a:
                        win_b = b
                        break  
                answer += 1
                B.remove(win_b)
        
            
    
    return answer
