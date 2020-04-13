#5:00
#무지의먹방라이브
from queue import PriorityQueue

food_times=[3, 1, 2]
k=5

def solution(food_times, k):
    #food_times : 먹을 음식의 각각 걸리는 시간을 저장해놓은 리스트
    #k : 네트워크 지연 시간
    answer = 0

    que=PriorityQueue() #우선순위 큐 사용, 먹는데 시간이 적게 걸리는 순서대로 음식 정렬하기 위해
    #입력 받아서 먹는데 시간이 적게 걸리는 순서대로 정렬
    for index,value in enumerate(food_times):
        que.put((value,index+1)) #이때, queue의 indxe로는 0번째 음식이 1번째 음식이기 때문에 +1해줌

    sum_food_time=0 # 지금까지 먹은 누적 시간
    current_que_length = len(food_times) #현재 남은 음식 개수
    previous_food_time=0 #이전에 먹었던 음식의 걸리는 시간 저장

    if sum(food_times)<=k: #전체 음식먹는데 걸리는 시간보다 k가 크면
        return -1

    while True: # 현재까지 먹은 누적 시간이 k를 넘지 않을 때 까지 반복

        #현재 남아있는 음식 개수 중 제일 시간이 적게 걸리는 것을 다 먹는데 걸리는 시간 계산
        food_time_to_eat_current_food_all=(que.queue[0][0]-previous_food_time)*current_que_length # (현재 먹은 음식에 걸리는 시간 - 이전에 먹은 음식의 걸리는 시간) * 현재 남아있는 음식 개수

        #이전까지 먹은 누적 시간 + 지금 음식 다 먹는데 거리는 시간의 합
        current_food_time = food_time_to_eat_current_food_all+sum_food_time
        if current_food_time >=k: # 만약 k보다 크면, 네트워크 지연 시간보다 더 걸리는 거니까 멈춰야함
            break

        que_first = que.get()[0] # 지금먹은 음식의 먹는데 걸리는 시간
        previous_food_time=que_first #이전에 먹은 음식의 걸리는 시간에 지금먹은 음식의 먹는데 걸리는 시간 저장
        sum_food_time+=food_time_to_eat_current_food_all # 지금까지 먹은 누적 시간에 현재 음식 먹는데 걸린 시간 더해줌
        current_que_length -= 1 #먹는데 제일 적게 걸리는 음식 다 먹었으니 전체 음식 개수 줄이기(전체 음식에서 다 먹은 음식 빼는거)

    #누적 시간이 k를 넘었을 때
    #queue(현재 남은 먹을 음식 담고있는거)를 다시 index 기준으로 정렬
    sorted_que=sorted(que.queue,key=lambda index: index[1])

    k-=sum_food_time # 네트워크 지연 시간에서 현재까지 음식먹었던 누적 시간을 빼줌(아까, 누적시간이 네트워크 지연 시간을 넘어가 버리면 그 때 먹으려고 했던 음식에서 다시 계산해주어야되서)
    target_index=k%current_que_length # 네트워크 지연이후 어떤 음식부터 먹어야 하는지 index계산
    answer=sorted_que[target_index][1] #계산한 index에 해당하는 실제 음식의 index값 찾기
    return answer

if __name__ == '__main__':
    print(solution(food_times,k))