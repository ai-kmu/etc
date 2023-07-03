class Solution:
    def continuousSubarrays(self, nums):
        n, total, l, dict1 = len(nums), 0, 0, defaultdict(int)

        for r in range(n):
            dict1[nums[r]] += 1

            while max(dict1.keys()) - min(dict1.keys()) > 2:
                dict1[nums[l]] -= 1

                if dict1[nums[l]] == 0:
                    del dict1[nums[l]]

                l += 1

            total += r-l+1

        return total
