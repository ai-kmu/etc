def solution (arrangement):
    
    answer = 0
    bar = 0
    arrangement = list(arrangement)
    
    while arrangement:
        if arrangement[0] == "(":
            bar += 1
            arrangement.pop(0)
            if arrangement[0]  == ")":  # 레이저
                bar -=  1 #레이저니 바 제거
                answer += bar # 레이저로 쪼개진 쇠막대기 add
                arrangement.pop(0)
        else:
            answer += 1  #  쇠막대기 하나 종료
            bar -= 1 # 종료된 쇠막대기 제외     
            arrangement.pop(0)
            
    return answer
