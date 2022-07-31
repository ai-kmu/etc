class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        now = max(nums[:k])
        answer = [now]
        print(answer)
        for i in range(len(nums)-k-k+1):
            if now < nums[k:k+i]:
                now = nums[k:k+i]
                answer.append(nums[k:k+i])
            else:
                answer.append(now)
        return answer
