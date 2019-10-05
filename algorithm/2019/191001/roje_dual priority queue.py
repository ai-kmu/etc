def solution(operations):
    answer = []
    for i in operations:
        # 명령어 데이터를 분리하여 command, data에 넣어주기
        command, data = i.split(" ")
        
        # command가 I일 경우
        if(command == "I"):
            # data를 넣어준다
            answer.append(int(data))
            
        else: # command가 D일 경우
            if(len(answer) == 0):
                continue
            # 그 중에서도 1일 경우
            if(data == "1"):
                # answer에서 최댓값을 삭제
                del answer[len(answer)-1]
                
            else: # -1일 경우
                # answer에서 최솟값을 삭제
                del answer[0]
                
        # answer을 sort하기
        answer.sort()
    
    if(len(answer) == 0):
        answer = [0,0]
    else:
        answer = [answer[len(answer)-1], answer[0]]
        
    return answer