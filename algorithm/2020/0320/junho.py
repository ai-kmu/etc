def solution(priorities, location):
    list = priorities
    answer = 0
    lonum = 0   # 각 우선순위에서 출력되는 마지막 index 저장 변수
    maximp = 9
    movelocation = location   #location 변동값 저장 변수
    objnum = list[location]   #목표 위치 우선순위
    for i in range(maximp,objnum,-1):    #높은우선순위 부터 목표위치값 이전까지
        tem = []
        for j,k in enumerate(list):
            if i ==k:   #해당 우선순위 index tem에 저장
                tem.append(j)
        if len(tem) > 0:
            tem.reverse()   #index 뒤에서 부터 처리하기 위해서
            answer += len(tem)
            lonum = tem[0]    #해당 우선순위중 마지막으로 출력되는 index
            for l in tem:   # list에서 출력될 index들을 제외하고 location 위치 조정
                if l < movelocation:
                    movelocation -= 1
                del list[l]
            movelist = lonum - len(tem) + 1
            list = list[movelist:] + list[:movelist]    #같은 우선순위중 마지막으로 출력되는 index이후부터 list 재정리
            if movelocation >= movelist:    #목표 위치조정
                movelocation -= len(list[:movelist])
            else:
                movelocation += len(list[movelist:])
    for i,j in enumerate(list):   #목표 위치에 해당 하는 우선순위 처리 
        if j == objnum:
            answer += 1
            if i == movelocation:
                break        
    return answer
