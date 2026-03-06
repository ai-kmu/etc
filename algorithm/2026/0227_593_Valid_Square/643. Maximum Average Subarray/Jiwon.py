class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 1:
            return max(nums)

        maxCandidates = deque(nums[:k])
        candidates = deque(nums[k:])

        currentSum = sum(maxCandidates)
        maxValue = currentSum

        while candidates:
            m = maxCandidates.popleft()
            a = candidates.popleft()
            maxCandidates.append(a)
            currentSum = currentSum - m + a

            if currentSum > maxValue:
                maxValue = currentSum

        return maxValue / k
