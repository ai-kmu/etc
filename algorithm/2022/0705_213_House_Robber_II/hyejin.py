class Solution:
    def rob(self, nums: List[int]) -> int:
        # 각 house마다 특정 money가 있음
        # 모든 house는 circle로 정렬 (첫번째와 마지막은 연결되어있음)
        # adjacent house는 연결되어 있음. 이중으로 털면 걸림
        # 털 수 있는 maximum cost
        n = len(nums)
        if n < 3:
            return max(nums)
        # 첫번째와 마지막이 맞닿아 있음. 0부터 n-2까지만 검사하면? 또는 반대로 해서 1부터 n-1까지만 구하면 되지 않을까?
        nums_reverse = nums[::-1]
        
        # 초기화
        answer = [0 for _ in range(n-1)]
        answer_reverse = [0 for _ in range(n-1)]
        
        # 먼저 0, 1번째 채워주기
        answer[0] = nums[0]
        answer[1] = max(nums[0], nums[1])
        answer_reverse[0] = nums_reverse[0]
        answer_reverse[1] = max(nums_reverse[0], nums_reverse[1])
        
        # 2부터 n-1까지 dp 수행
        # answer의 i번째는 0부터 i번째까지 maximum cost를 계산
        for i in range(2, n-1):
            answer[i] = max(answer[i-2] + nums[i], answer[i-1])
            answer_reverse[i] = max(answer_reverse[i-2] + nums_reverse[i], answer_reverse[i-1])
            
        return max(answer[-1], answer_reverse[-1])
            
