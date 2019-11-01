def solution(A, B): 
    answer = 0
    sortA = sorted(A)
    sortB = sorted(B)
    for i in range(len(sortA)):
        for j in range(len(sortB)):
            if(sortB[j]>sortA[i]):
                answer += 1
                del sortB[j]
                break
    return answer