import math

def solution(progresses, speeds):
    answer = []
    remains = list(map(lambda x: 100-x, progresses))                # 남은 작업진도 구하기
    dates = list(map(lambda x,y: math.ceil(x/y), remains, speeds))  # 배포까지 남은 일수 구하기(remains/dates 값을 올림)
    
    while dates != []:        # dates가 빈 리스트가 되기 전까지
        count = 0             # 각 loop마다 count 초기화
        for d in dates:       # dates의 첫번째 원소부터 차례대로
            if d <= dates[0]: # 첫번째 원소보다 작거나 같은 애들만 count
                count += 1
            else:             # 첫번째 원소보다 큰 애가 나타나면
                break         # break하고
        answer.append(count)  # count를 answer에 append하고
        dates = dates[count:] # dates 중 남은 애들만 다시 dates에 할당하고 다시 반복
        
    return answer
