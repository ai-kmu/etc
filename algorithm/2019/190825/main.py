def solution(n):
    answer = " "
    
    while n > 0:
        n = n - 1
        answer = '124'[n%3] + answer
        
        n = n / 3
    
    return answer
