def solution(priorities, location):
    answer = 0
    p = priorities
    
    for i in range(len(p)):
        if location == i:
            #튜플 이용해서 배열 묶기(해당 location일때 1)
            p[i] = (p[i], 1)
        else:
            #나머지는 다 0
            p[i] = (p[i], 0)
            
    #첫번째 인쇄목록 가져오기
    while True:
        idx = 0;
        target = p[0][0]
        result = p[0][1]
        
        #중요도 가장 높은 인쇄물 찾기
        for j in range(len(p)):
            if target < p[j][0]:
                target = p[j][0]
                result = p[j][1]
                idx = j
                #가장 중요도 높은 인쇄물의 인덱스 저장
        
        #현재 result값이 내가 알고 싶은 인쇄물 일 때
        if result == 1:
            return answer + 1
            #첫번째로 인쇄할 목록
        
        #첫번째로 인쇄할 목록 일 때
        if idx == 0:
            del p[0]
            answer = answer + 1
            #인쇄순서 1증가
        else: 
            p.append(p[0])
            del p[0]
        #삭제하고 첫번째를 가장 마지막 대기열로 보내기
        
    return answer
