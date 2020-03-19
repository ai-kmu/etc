def solution(priorities, location):
    q = []
    answer = {}
    prior = 1
    
    for loc, importance in enumerate(priorities):
        q.append([importance, loc])
        
    while(q):
        # 대기목록에 문서가 하나만 남았을 경우
        if prior == len(priorities):
            importance, loc = q.pop(0)
            answer[loc] = prior
            break
    
        importance, loc = q.pop(0)
        max_q = max(q)
    
        # 나머지 인쇄대기 목록에 중요도가 더 높은 것이 있다면
        if importance < max_q[0]:
            # 현재 문서를 대기 순서 가장 끝으로 지정
            q.append([importance, loc])

        # 지금 문서가 나머지 문서들보다 중요도가 높은 것이라면
        else:
            # 현재 문서를 인쇄
            answer[loc] = prior
            prior += 1
    
    return answer[location]

# 가장 괜찮다고 생각하는 방법
def solution(priorities, location):
    ans = 0
    m = max(priorities)
    while True:
        v = priorities.pop(0)
        if m == v:
            ans += 1
            if location == 0:
                break
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(v)
            if location == 0:
                location = len(priorities)-1
            else:
                location -= 1
    return ans
