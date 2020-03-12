import math
def solution(progresses, speeds):
    answer = []
    tem = 0     # 한번에 배포할 기능 수를 저장할 변수
    publish_day = 0     # 앞선 기능이 완성 될 날짜 저장할 변수
    
    for i in range(0,len(progresses)):
        complete_day = math.ceil((100 - progresses[i]) / speeds[i])     # 기능 완성되는 날짜
        if publish_day < complete_day :     #후의 기능들이 앞선 기능보다 늦게 완성되어야 다른 날짜에 배포가 됨
            publish_day = complete_day
            answer.append(tem)      #같은 날에 배포될 기능들의 수를 answer에 추가
            tem = 0     #초기화
        tem +=1
    answer.append(tem)      # 마지막에 배포될 기능들 answer에 추가
    answer.pop(0)       # 반복문 첫번째에 tem =0인 값이 append되므로 제거
    return answer
