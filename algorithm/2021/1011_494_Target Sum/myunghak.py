# dfs로 완전 탐색 함
# 중간에 불가능할 것 같은 상황(나머지를 다 더하거나 빼도 traget 보다 작거나 클 때)에는 탈출
# 불가능할 것 같은 상황을 최대한 빠르게 탐지하기 위해 내림차순 정렬

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int):
        nums.sort(reverse= True) # 내림 차순 정렬해야 18번줄에 최대한 빨리 걸려 시간 절약 함
        nums_length = len(nums)

        # summation 미리 계산, 최대한 빠르게 하기 위해 미리 sum 계산해놓고 끝에서부터 뺌
        sum_ = sum(nums)
        summation = []
        for d in nums:
            summation.append(sum_)
            sum_ -=d
        
        def search(sum_, idx, ans): # dfs로 완전 탐색
            if nums_length == idx+1:
                return ans + (sum_ + nums[idx] == target) + (sum_ - nums[idx] == target)
            elif sum_ + summation[idx] < target or sum_ - summation[idx] > target:
                return ans
            
            return search(sum_ + nums[idx], idx+1, ans) + search(sum_ - nums[idx], idx+1, ans)

#         ans = search(-nums[0], nums[1:], ans, [-nums[0]])
        return search(0, 0, 0) # dfs로 완전 탐색
        
        
