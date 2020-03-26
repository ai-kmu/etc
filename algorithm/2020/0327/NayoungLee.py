def solution(arrangement):
    answer = 0
    s = arrangement
    thick = 0 # 두께
    flag = 0 # 최근에 괄호가 뭐가 나왔는지
    
    for i in range(0,len(s)):
        if s[i] == '(' : 
            # 여는 괄호라면, 두께를 1 추가
            thick = thick + 1
            flag = 0
        else :
            # 닫는 괄호라면 두께를 1 감소
            thick = thick - 1 
            # 레이저 일 때
            if flag == 0: 
                answer = answer + thick
            # 레이저가 아닌경우 (자연스럽게 쇠길이가 끝나서 조각이 생긴 것)
            else : 
                answer = answer + 1
            flag = 1
    return answer
