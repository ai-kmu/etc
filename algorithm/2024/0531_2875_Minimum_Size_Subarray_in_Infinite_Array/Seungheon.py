# 풀다 실패

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        

        nums_sum = sum(nums)
        list_a = [0]
        list_b = [0]

        for i in range(len(nums)):
            list_a.append(nums[i]+list_a[i])
            list_b.append(nums[-i-1]+list_b[i])

        if nums_sum // target * 2 > 0:
            answer = (nums_sum // target)*len(nums) + 1
            target = nums_sum % target + nums_sum
        else:
            answer = 0

        min_sum_indices = None
        min_index_sum = nums_sum * 2

        a_idx = 0
        b_idx = len(nums) - 1

        while a_idx < len(nums) and b_idx >= 0:
            current_sum = list_a[a_idx] + list_b[b_idx]
            if current_sum == target:
                current_index_sum = a_idx + b_idx
                if current_index_sum < min_index_sum:
                    min_index_sum = current_index_sum
                    min_sum_indices = a_idx + b_idx
                if a_idx + 1 < len(nums) and b_idx - 1 >= 0:
                    if list_a[a_idx + 1] + list_b[b_idx - 1] <= target:
                        a_idx += 1
                    else:
                        b_idx -= 1
                else:
                    break
            elif current_sum < target:
                a_idx += 1
            else:
                b_idx -= 1

        return min_sum_indices + answer if min_sum_indices is not None else -1
