def solution(n, t, m, p):
    
    def transform(num, b): # 10진수 -> n진수
        temp = '0123456789ABCDEF'
        
        q, r = divmod(num, b)
        
        return transform(q, b) + temp[r] if q else temp[r]
    
    number = ''
    
    k = 0
    
    while len(number) < m*t: # 미리 준비할 숫자까지만 n진법으로 구하면 됨.
        
        number += transform(k, n)
        k += 1
    # 숫자가 다 구해졌다면
    answer = ''
    
    k = 0
    
    while len(answer) < t: # t개가 될 때 까지
        
        answer += number[k*m + p - 1] # 주인공이 구해야할 문자들만 쏙 빼내옴
        k += 1    
    
    return answer
