def solution(numbers, target):
    answer = 0
    
    # 현재까지 계산된 값들을 넣는 리스트
    leaves = [0]
    
    # 숫자들을 돌며 +, -한 값을 모두 leaves에 저장
    for num in numbers:
        
        # tmp는 현재 leaves에 있는 숫자에서 +, - 한 것 모두 계산한 리스트
        tmp = []
        for parents in leaves:
            tmp.append(parents + num)
            tmp.append(parents - num)
        leaves = tmp
    
    # 마지막으로 leaves를 모두 돌며 target과 같다면 answer에 1 더해주기
    for leaf in leaves:
        if leaf == target:
            answer += 1
            
    return answer
