from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # 자동 정렬해주는 SortedList선언 -> subarray에서 min, max구할 때 사용
        min_max = SortedList()
        ans = 0
        left_idx = 0

        # nums를 돌며 sorted list에 각 원소를 더해줌
        for i in range(len(nums)):
            min_max.add(nums[i])
            # 최대 - 최소가 2보다 큰 subarray를 찾아서 먼저 더해줌
            while min_max[-1] - min_max[0] > 2: 
                min_max.remove(nums[left_idx]) 
                ans += i - left_idx
                left_idx += 1
        # max - min이 2이상 차이가 나지 않는 subarray들을 한번에 처리 
        for x in range(left_idx, len(nums)):
            ans += len(nums) - x
        return ans
