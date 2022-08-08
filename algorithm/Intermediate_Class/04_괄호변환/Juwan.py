def solution(p):
    
    def is_balance(in_str): # 균형 검사
        
        if len(in_str)/2 == in_str.count('('):
            return True
        else:
            return False
        
    def is_correct(in_str): # 올바른 괄호 검사
        
        budget = 0
        
        for i in in_str:
            if budget < 0:
                return False
            
            if i == '(':
                budget += 1
            elif i == ')':
                budget -= 1
        
        return True
    
    
    def recur(in_str): # 그냥 문제에 나와있는 로직을 따라 구현한 재귀함수..
        
        if in_str == '':
            return ''
        
        cnt = 1
        
        while True:
            
            if is_balance(in_str[:cnt]):
                break
            else:
                cnt += 1
                
        u = in_str[:cnt]
        v = in_str[cnt:]
        
                
        if is_correct(u):
            return u + recur(v)
        else:
            temp = '(' + recur(v) + ')'
            reverse_u = ''
            
            u = u[1:-1]
            
            
            for j in u:
                if j == '(':
                    reverse_u += ')'
                elif j == ')':
                    reverse_u += '('
            
            return temp + reverse_u
            
    
    answer = recur(p)
    return answer
