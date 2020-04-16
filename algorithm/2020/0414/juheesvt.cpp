from queue import PriorityQueue
def solution(food_times, k):
    # 만약 더 섭취해야할 음식이 없다면 -1
    # k라는 시간 보다 food_times 전체 합보다 크거나 같으면 -1
    if sum(food_times) <= k:
        return -1
    
    answer = 0
    
    # Priority Queue는 값을 뺄 때 오름차순 정렬되어 가장 적은 값을 버린다.
    q = PriorityQueue()
    for i in range(len(food_times)):
        q.put((food_times[i], i+1)) # Priority Queue를 활용, (food_times, index)를 넣는다.
    
    sum_value = 0 # 누적되는 k에서 빼지는 값
    previous = 0 # 이전에 다 먹은 음식 값
    length = len(food_times) # 전체 음식 개수
    # print(q.queue)
    
    # 현재 상황에서 음식을 다 먹어서 뺄 수 있는지 k랑 비교해야 한다.
    # sum_value와 빼버릴 음식의 시간-이전 음식 값 * 현재 음식 개수와 비교
    while sum_value + ((q.queue[0][0] - previous) * length)<= k:
        now = q.get()[0] # 제일 적은 시간으로 걸린 것부터 Queue에서 빼자.
        # 뺀다는 것은 전체 한 바퀴를 돌아야한다.
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식을 빼게 되므로 전체 길이는 -1만큼 줄어든다.
        previous = now # 이전 과일을 업데이트 한다. 
    
    # q.queue를 인덱스 기준으로 다시 정렬한다.
    result = sorted(q.queue, key=lambda x:x[1])
    # 최종적으로 남은 음식 중에서 현재 k가 몇 번째 음식인지 확인해야 합니다. (k - sum_value)% length
    return result[(k - sum_value) % len(q.queue)][1]
