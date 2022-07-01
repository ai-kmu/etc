class Solution(object):
    def rob(self, nums):
        # 각 point에서 최대로 얻을 수 있는 money 조사
        # 첫번째 값을 사용했을때와 사용하지 않았을때의 값을 비교하여 이웃한 값을 사용했는지 확인
        
        # 예외처리
        if len(nums) == 1:
            return nums[0]
        
        # first_time = True : 첫번째 값을 사용하는 경우
        # first_time = False : 첫번째 값을 사용하지 않는 경우 
        def dp_max(nums, first_time = True):
            dp = [ 0 for _ in range(len(nums)) ]
            # '전전값 + 현재값' 이 '전값' 보다 크면
            for i in range(len(nums)):
                # 전전 값 인덱스
                prvprv_i = (i + len(nums) - 2)%len(nums)
                # 전 값 인덱스
                prv_i = (i + len(nums) - 1)%len(nums)
                # 마지막 값 사용
                if dp[prvprv_i] + nums[i] > dp[prv_i]:
                    # 마지막값을 사용했다면, 
                    # 첫값을 사용하지 않았을때 의값과, 마지막값을 사용하지 않았을떄의 값을 비교
                    if first_time == True and i == len(nums) - 1:
                        no_used_first = dp_max(nums[1:], False)
                        if dp[prvprv_i] + nums[i] == no_used_first:
                            dp[i] = dp[prvprv_i] + nums[i] 
                        else:
                            dp[i] = max(dp[prv_i], no_used_first)
                    else:        
                        dp[i] = dp[prvprv_i] + nums[i]      
                # 마지막 값 사용하지 않음
                else:
                    dp[i] = dp[prv_i] 
                   
            return dp[-1]
        
        return dp_max(nums)
