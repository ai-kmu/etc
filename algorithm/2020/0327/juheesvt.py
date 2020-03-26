def solution(arrangement):
    
    answer = 0                  # 최종적으로 반환 될 총 막대의 갯수
    is_pass = False             # 레이저가 나오면 그 다음 인덱스로 넘어가기 위한 변수
    stick = 0                   # 현재 레이저 아래에 있는 막대의 갯수
    size = len(arrangement)     # 입력되는 리스트의 사이즈
    
    for i in range(size) :
        
        # 만약 is_pass 면, 레이저였기 때문에 아래 코드를 실행하지 않고 i를 증가시킨다.
        if is_pass : 
            # 다음에는 아래 코드를 실행시키기위해 False로 바꿔줌
            is_pass = False     
            continue
            
        if arrangement[i] == '(' :
            if arrangement[i+1] == ')' :
                
                # 레이저가 나오면, 레이저 아래에 있는 막대의 갯수를 더해 준다.
                answer += stick
                is_pass = True
                continue
            
            # '('  입력이 연속으로 들어오면 막대의 개수를 추가한다.
            else :
                stick += 1
        
        # ')' 입력이 연속으로 들어오면 레이저 아래의 잇는 막대의 개수는 하나 줄여준다.
        # 하지만 막대 생성(?)이 끝난 것이기 때문에 총 막대는 1개 늘어나야 한다.
        else :
            stick -= 1
            answer += 1                   
    
    return answer
