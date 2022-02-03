## 풀이 방식: 위의 조건을 변형하면 nums[i] - rev(nums[i]) == nums[j] - rev(nums[j]) 
## 위이 같은 수식을 통해서 자기 자신의 역수를 뺸 값들이 같다면 pair로 가능함
 
def countNicePairs(nums):
    count = 0            # nice pair 초기값 할당
    modulo = 10**9 + 7  # 조건(pair 개수가 너무 많을 경우 할당)
     
    state = {}           # 값의 차이를 저장할 dictionary 정의
    n = len(nums)        # 전체 입력 데이터 수 
    
    for i in range(n):    
        diff = nums[i] - int(str(nums[i])[::-1]) # 입력 데이터별로 값 - 역수 값 계산
        stat[diff] = stat.get(diff, 0) + 1       # (값 - 역수 값) 계산 후 결과를 dictionary의 저장
        
        ## dictionary에서 두 값의 차이(값, 역수의 값) 개수 확인
        if stat[diff] > 1:
            count += stat[diff] - 1              # 같은 차이 만큼 count 더함
            
        ## condition: that number can be too large, return it modulo 10^9 + 7
        if (count / modulo) >= 1:
            count = module
        
    return count
