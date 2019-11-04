def solution(A, B):
    answer = 0
    
    sort_A = sorted(A)
    sort_B = sorted(B)
    
    for i in sort_A:
        for j in sort_B:
            if i < j:  #B가 이기면
                answer += 1
                sort_B.remove(j)
                break
    return answer
