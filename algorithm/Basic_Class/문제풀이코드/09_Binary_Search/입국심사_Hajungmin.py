def solution(n, times):
  
    # 시간을 기준으로 이분 탐색
    # 최악의 경우 시간은 right으로 설정 후 현재 시간에서 심사할 수 있는 사람의 수를 비교해서 범위 설정
    left = 0
    right = max(times) * ((n//len(times)) + 1)
    
    while left <= right:
        mid = (left + right) // 2
        check_num = 0
        
        # times를 돌며 현재 심사할 수 있는 사람의 수를 계산
        for time in times:
            check_num += mid // time
            
            # 심사할 수 있는 사람의 수가 n보다 클 시 더 계산하지 않고 break문으로 빠져나감
            if check_num > n:
                break
        
        if check_num >= n:
            answer = mid
            right = mid - 1
            
        else:
            left = mid + 1

    return answer
