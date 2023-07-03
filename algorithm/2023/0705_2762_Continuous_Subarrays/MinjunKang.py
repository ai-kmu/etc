# 구현 실패
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        a = len(nums)

        cnt = 0
        ans = 0
        while a > 0:

            tmp = []
            for i in range(a-1):
                diff = nums[i+1]-nums[i]
                tmp.append(diff)
            nope = []
            for j, v in enumerate(tmp):
                if v > 2:
                    nope.append(j)


            if not nope:
                t = len(tmp) - (len(nums)-cnt) + 1
                ans += t
            a -= 1
            nums = tmp
            cnt += 1
        
        return ans
