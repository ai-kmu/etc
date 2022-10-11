def solution(numbers, target):
    # bfs, 모든 노드를 하나씩 더하거나 빼가며 순차적으로 갱신
    # 최종 노드를 만들때 리프노드에서 탐색하여 같은 값이 있으면 answer를 더해줌
    answer = 0
    # 뿌리노드를 0으로
    ans_list = [0] 
    # number의 값을 통해 더하거나 빼주면서 뿌리를 뻗어나감
    for num in numbers: 
        temp = []
        for an in ans_list:
            temp.append(an + num)
            temp.append(an - num)
        ans_list = temp
    
    # 최종 여부 확인
    for ans in ans_list:
        if target == ans:
            answer += 1
    
    
    return answer
