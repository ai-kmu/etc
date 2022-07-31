#시간초과
#max연산을 최대한 줄여보려 했으나 잘 안됐음
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxTemp = max(nums[:k])
        res.append(maxTemp)
        for i in range(1, len(nums)-k+1):
            if maxTemp > nums[i+k-1] and maxTemp != nums[i-1]:
                res.append(maxTemp)
            else:
                maxTemp = max(nums[i:i+k])
                res.append(maxTemp)
        return res
