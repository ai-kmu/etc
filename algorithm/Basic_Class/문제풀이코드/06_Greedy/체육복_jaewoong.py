def solution(n, lost, reserve):
    answer = []
    
    # 제한사항 5번에 대한 예외처리를 적용한 집합
    set_lost = set(lost) - set(reserve)
    set_resurve = set(reserve) - set(lost)
    
    # 자기 번호보다 크거나 작은 사람이 있는경우
    # 해당 번호를 지운다(=빌려준다)
    for r in set_resurve:
        if r-1 in set_lost:
            set_lost.remove(r-1)
        elif r+1 in set_lost:
            set_lost.remove(r+1)
            
    # 전체학생의 수 - 잃어버렸는데 빌려서 채워진 수
    answer = n - len(set_lost)
    
    return answer
