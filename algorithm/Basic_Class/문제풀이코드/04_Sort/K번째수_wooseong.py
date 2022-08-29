def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # 잘라서 정렬
        temp = sorted(array[i-1:j])
        # k번째 answer에 저장
        answer.append(temp[k-1])
    
    return answer
