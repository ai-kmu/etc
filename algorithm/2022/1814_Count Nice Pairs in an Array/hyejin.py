from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        answer = 0
        
        # 이중 for문은 시간초과
        # nums[i] - rev(nums[i]) == num[j] - rev(nums[j])를 이용
        # O(N) 걸림
        # 먼저 nums[i] - rev(nums[i])를 계산 
        # diff의 빈도를 계산
        diff_dict = defaultdict(int)
        for num in nums:
            diff = num - int(str(num)[::-1])
            diff_dict[diff] += 1
        
        # 각 key에 담겨져 개수(같은 diff를 가진 element의 개수)를 이용하여 nC2으로 쌍 개수 계산
        # nC2 = n(n-1)/2
        for value in diff_dict.values():
            answer += value * (value-1) // 2
        
        return answer % (10**9 + 7)
