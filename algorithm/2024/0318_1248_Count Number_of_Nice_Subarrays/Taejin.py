class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_pos = [-1] # start position

        for i in range(len(nums)): # append odd position
            if nums[i] % 2 == 1:
                odd_pos.append(i)

        odd_pos.append(len(nums)) # end position

        if len(odd_pos) < k + 2:
            return 0

        else:
            ret = 0

            for pivot in range(1, len(odd_pos) - k): # count all possible interval cases
                ret += (odd_pos[pivot] - odd_pos[pivot - 1]) * (odd_pos[pivot + k] - odd_pos[pivot + k - 1])

            return ret
