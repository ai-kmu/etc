class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() # n(log n)
        
        # 처음 answer
        answer = nums[0] + nums[1] + nums[2]
        
        # 3중 for loop solution은 시간 초과
        
        # 이 soluntion은 n^2? worst case는 n^2?
        # for loop
        for i in range(len(nums)):
            l = i + 1 # left
            r = len(nums) - 1 # right
            while l < r: # left < right
                s = nums[l] + nums[r] + nums[i] # three sum
                if s == target: # 우리가 원하는 답 (가장 가깝다면)
                    return target
                else:
                    answer = answer if abs(answer - target) < abs(s - target) else s # current answer와 비교
                    if s > target: # target보다 크면 r을 줄인다.
                        r -= 1
                    else: # target보다 작다면 l을 늘린다.
                        l += 1
        
        return answer
        
