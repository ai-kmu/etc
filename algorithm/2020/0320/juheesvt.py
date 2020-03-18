def solution(priorities, location):
    
    cnt = 1
    papers = [(priorities[i],i) for i in range(len(priorities))]  # (우선순위, 인덱스)
    
    while len(papers) > 0 :
        current = papers[0]        
        for paper in papers[1:] :
            if current[0] < paper[0] :
                papers.append(current)
                break
        else:
            if current[1] == location :
                return cnt
            cnt+=1            
        papers = papers[1:]
            
