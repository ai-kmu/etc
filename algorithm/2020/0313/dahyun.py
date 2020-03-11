def solution(progresses, speeds):
    
    import math
    
    answer = []
    remains = list(map(lambda x: 100-x, progresses))                # 남은 작업진도 구하기
    dates = list(map(lambda x,y: math.ceil(x/y), remains, speeds))  # 배포까지 남은 일수 구하기(remains/dates 값을 올림)
    
    while dates != []:        # dates가 빈 리스트가 되면 stop
        dates = list(map(lambda x: x-dates[0], dates))  # dates의 첫번째 원소를 각 원소에서 빼서 다시 dates에 할당
        count = 0             # 각 loop마다 count 초기화
        for d in dates:       # dates의 첫번째 원소부터
            if d <= 0:        # 0 이하인 애들만 count
                count += 1
            else:             # 0 초과인 애가 나타나면
                break         # break하고
        answer.append(count)  # count를 answer에 append하고
        dates = dates[count:] # dates 중 남은 애들만 다시 dates에 할당하고 다시 반복
        
    return answer
