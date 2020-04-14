# 정확도 통과, 효율성 통과 못함
def solution(food_times, k):
    time = 0
    while True:
        for ind in range(len(food_times)):
            if sum(food_times) == 0:  # 해당 시간 이전에 음식 
                return -1
            
            if food_times[ind] > 0 :  
                food_times[ind] -= 1 # 해당 index 음식 다 먹은게 아니면 음식 섭취 -1
                time += 1  # 시간 add
                if time == k+1:  #시간이 다됬으면 멈추고
                    return ind + 1 # 해당 인덱스 출력
            
