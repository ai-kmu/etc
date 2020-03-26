def solution(arrangement):
    # answer : 쇠막대기의 조각 수
    answer = 0
    # lines : 더해줘야하는 막대기 수를 
    lines = 0
    # idx : index를 나타냄
    idx = 0
    
    while True:
        # idx가 마지막 index가 아닐 때
        if idx+1 < len(arrangement):
            
            # () : laser일 경우 idx를 하나 건너 뛰어주기 위해 더하고
            # laser 이전의 막대 개수 만큼 answer에 더해줌
            if arrangement[idx] == '(' and arrangement[idx+1] == ')':
                idx += 1
                answer += lines
                
            # ( : 왼쪽괄호의 시작일 경우
            # lines에 1을 더해줌
            
            elif arrangement[idx] == '(' and arrangement[idx+1] != ')':
                lines += 1
            # ) : 오른쪽 괄호일 경우
            # lines에 1을 빼주고
            # answer에 1을 더해줌
            elif arrangement[idx] == ')':
                lines -= 1
                answer += 1
                
        # idx가 마지막 index일 경우 (')')
        # answer에 1을 더하고 break
        else:
            answer += 1
            break
        idx += 1
        
    return answer
