# fail code - time limit

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        answer = 0
        # 시작위치
        for i in range(len(nums)):
            sub_max = nums[i]
            sub_min = nums[i]
            # sub_list길이
            for j in range(i, len(nums)):
                sub_max = max(sub_max, nums[j])
                sub_min = min(sub_min, nums[j])
                if abs(sub_max - sub_min) <= 2:
                    answer += 1
                else:
                    break

        return answer
