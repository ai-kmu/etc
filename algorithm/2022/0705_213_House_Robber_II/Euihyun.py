# 오답...
# 원으로 연결된 상황의 dp를 구현하지 못함
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 리스트 갯수 확인
        n= len(nums)   
        # 원으로 연결되어 있기 때문에 3이하의 수가 들어오면 최대값이 가장큼
        if n <= 3:
            return(max(nums))
        
        # 아닌경우 dp로 계산
        else:
            # n개 생성후 0과 1은 대입
            dp = [0] * (n)
            dp[0] = nums[0]
            dp[1] = nums[1]
            
            # 2번부터 시작해서 이전값과 -2번째 값+i 해서 큰 값을 저장
            for i in range(2,n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
            # 맥스값 반환
            return(max(dp))
        
