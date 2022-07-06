class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # 집 3개까지는 money 가장 큰 값
        if len(nums) <= 3:
            return max(nums)
        
        # 첫번째 집 방문 - 마지막 집 X
        dp_f = [0] * (len(nums)-1)
        # 마지막 집 방문 - 첫번째 집 X
        dp_e = [0] * (len(nums)-1)
        
        dp_f[0] = nums[0]
        dp_f[1] = max(nums[0], nums[1])
        
        dp_e[0] = nums[1]
        dp_e[1] = max(nums[1], nums[2])
        # 점화식: 하나 건너서 방문할 수 있기에, 현재 i는 이전 i-1 <> i-2 + i번 money 중 큰 값 선택  
        # dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        
        for i in range(2, len(nums)-1):
            dp_f[i] = max(dp_f[i-1], dp_f[i-2]+nums[i])
        for i in range(2, len(nums)-1):
            dp_e[i] = max(dp_e[i-1], dp_e[i-2]+nums[i+1])
        return max(dp_f[-1], dp_e[-1])

# dp 대신 시도했던 코드, 짝수 10에서 예외에 걸린다
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        tmp = []
        
        # len(nums) 짝수일 때, 최대값 계산 함수
        def evenSum(n):
            odd = 0
            even = 0
            for i in range(len(n)):
                if (i%2) == 0:
                    odd += n[i]
                else:
                    even += n[i]
            return max(odd, even)
        
        # nums 길이가 짝수이면, 최대값 계산 함수 호출  
        if len(nums) % 2 == 0:
            return evenSum(nums)
        
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 3:
            return max(nums)
        
        # nums 길이가 홀수이면, len(nums) 짝수로 만들고, 계산 함수 호출
        for i in range((len(nums)//2)+1):
            standard = nums[i]
            copy = nums[:]
            copy.pop(i+1)
            copy.pop(i)
            copy.pop(i-1)
            tmp.append((standard + evenSum(copy)))
            
        return max(tmp)
'''            
