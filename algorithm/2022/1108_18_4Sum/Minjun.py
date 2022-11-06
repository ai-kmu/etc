# 중복처리 안 됨,,
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        answer = []
        
        for i, a in enumerate(nums):
            if i > len(nums)-4:
                break
            for j, b in enumerate(nums[i+1:]):
                for k, c in enumerate(nums[i+2:]):
                    for l, d in enumerate(nums[i+3:]):
                        if a+b+c+d == target:
                            tmp = [a,b,c,d]
                            tmp.sort()
                            if tmp not in answer:
                                answer.append(tmp)
                        
        return answer
