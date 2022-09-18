def solution(n, lost, reserve):
    
    # 진짜 빌려줄수 있는 친구와 진짜 잃어버린 친구 set을 통해서 구함
    reserve_on = set(reserve) - set(lost)
    lost_on = set(lost) - set(reserve)
    
    # 진짜 빌려줄수 있는 친구중 앞뒤에 잃어버린 친구가 있으면 빌려줌
    for i in reserve_on:
        front = i - 1
        back = i + 1
        if front in lost_on:
            lost_on.remove(front)
        elif back in lost_on:
            lost_on.remove(back)
            
    # 마지막까지 받지못한 사람의 수를 전체에서 뺌
    return n - len(lost_on)
