'''

풀이 과정 
=> player01부터 시작하여 양끝을 뽑고 이후 player 1이 뽑으면 결과값을 비교해 최적값을 반환 

'''

class Solution:
    def PredictTheWinner(self, nums):

    # 필요 함수 정의(start의 의미: 뽑는쪽 => 0일 경우는 player 1 / 1인 경우 player 2)
    def solve(nums, i, j, start):
       
        ## 뽑는 위치 i 끝단이 j보다 높을 경우는 다 뽑았기 때문에 값을 0으로 반환
        if i > j:
            return 0

        ## player 1인 경우는 양쪽에서 뽑을 때 최대값으로 뽑음
        if start == 0:
            return max(nums[i] + solve(nums, i+1, j, 1), nums[j] + solve(nums, i, j-1, 1))
        
        ## player 2인 경우는 양쪽에서 뽑을 떄 최소값을 뽑음 
        else:
            return min(solve(nums,i+1,j,0), solve(nums,i,j-1,0))
            
        
    # 필요 변수 정의
    player01, player02 = 0, 0 
    n = len(nums)
    
    # player 02 총합을 더함 => 이후 player01 값을 빼면서 값들을 비교 진행
    for num in nums:
        player02 += num
    
    # play01 값을 구함
    player01 = solve(nums, 0, n-1, 0)
    
    # player02 값을 총합에서 player 01 뺴줌
    player02 -= player01
    
    # 두값을 비교해서 결과 도출(player01이 높으면 True)
    if player01 >= player02
        return True
    else:
        return False
