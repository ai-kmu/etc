class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        answer = set([])

        for i in range(n):
            for j in range(i+1, n):
               k = j + 1
               d = n - 1

               now = target - nums[i] - nums[j]

               while k < d:
                    if nums[k] + nums[d] == now:
                       answer.add((nums[i], nums[j], nums[k], nums[d]))
                       k += 1
                       d -= 1
                    elif nums[k] + nums[d] < now:
                        k += 1
                    else:
                        d -= 1
        
        return answer
