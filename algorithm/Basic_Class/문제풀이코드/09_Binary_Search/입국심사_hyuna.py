def solution(n, times):
    answer = 0
    
    # 시간의 start, end 
    s = 0
    e = max(times) * n
    
    while (True):
        # 중간 값 계산 (시간)
        mid = (s + e) // 2
        # 해당 시간에 심사받을 수 있는 사람 수 저장할 변수
        count = 0
        
        # mid 시간에서 총 검사받을 수 있는 사람을 계산
        for i in times:
            count += (mid // i)
        
        # 사람 수가 n보다 많으면 반 나눈 것에 왼쪽에 적정 시간이 있을거고
        # 사람 수가 n보다 적으면 반 나눈 것에 오른쪽에 적정 시간이 있어서 s 와 e 값 조절 
        if n <= count:
            e = mid
        elif n > count:
            s = mid 
            
        # s 와 e-1이 같을 때 시간이 찾아진 것이므로 저장하고 반복문 빠져나옴 
        if s == e-1:
            answer = e
            break
        
    return answer 
