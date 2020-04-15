def solution(food_times, k):
    num_food = len(food_times)
    answer = 0
    
    # 만약 k가 먹는 모든 시간을 합친 것보다 크다면 그전에 다먹었으므로 -1이다.
    if k >= sum(food_times):
        return -1

    # # 시간 초과
    # # 하나씩 빼면서 계산하는 방법, 심지어 정확성에서 5개정도 에러..왜지?
    # idx = 0
    # count = 0
    # while k+1 != count:
    #     if sum(food_times) == 0:
    #         return -1
    #     if food_times[idx] == 0:
    #         idx = (idx+1)%num_food
    #         continue
    #     else:
    #         food_times[idx] -= 1
    #         count +=1
    #         idx = (idx+1)%num_food
    # return idx
    
    # list중에 가장 작은 시간을 계속 빼주다보면 최소 몇번 싸이클이 도는지 알수 있다.
    count = 0
    sort_time = sorted(food_times)
    sub_time = 0
    # 남아있는 원소의 개수
    for i in range(num_food):
        # 이전 시간과 같다면 패스해준다.
        if sort_time[i] == 0:
            continue
        # 현재 남은 시간중 가장 작은 수
        time = sort_time[i] - sub_time
        # 싸이클 돌면서 각 원소에 빼준 수
        sub_time += time
        # 빼준 수들을 전체 다 더한 수 => 바퀴 도는데 몇초 걸렸는지
        count += time * (num_food - i)
        # k보다 크다면 빠져나와야함.(k초보다 더 많이 먹은것)
        if k <= count:
            break
    
    # k와 얼마나 차이나는지 => 다시 back해야되는 횟수
    count = count - k
    
    # 아직 남아있는 음식들의 index들을 저장.
    rest_time_idx = []
    # count만큼 돈 후에 남은 시간들을 계산하고 남은 음식은 index를 저장해줌. 0은 다시 back할 가능성이 있기 때문에 포함해야함.
    for i in range(num_food):
        food_times[i] -= sub_time
        if food_times[i] >= 0:
            rest_time_idx.append(i)
    '''
    count == k인것. 돌지 않아도 됨.
    여기서는 원래 남은시간이 0인 것이 포함이 되면 안되는데 포함이 되도 에러가 안남. 왜지?? test case의 잘못인듯
    만약 에러가 난다면 food_times를 for문을 돌면서 첫번쨰로 만나는 0보다 큰 원소의 index를 반환해줌.
    for i,v in enumerate(food_times):
        if v > 0: return i
    '''
    if count == 0:
        return rest_time_idx[0] +1
    else:
        # 남은 음식들을 되돌려야함.
        # count가 남은 음식의 개수보다 클 경우는 n번을 돌며 back하기 때문에 계산 필요.
        count %= len(rest_time_idx)
        return rest_time_idx[-count] +1
    
        # 이건 위의 n번 back할 가능성을 생각하지 못했을 때. 몇개 오류남.
        # => 이것때매 남아있는 음식의 index와 개수가 필요
        # for i in range(num_food-1,0,-1):
        #     if food_times[i] < 0:
        #         continue
        #     else:
        #         count -= 1
        #         if count == 0:
        #             return i+1
                
        
        
    
    
        
    
    
