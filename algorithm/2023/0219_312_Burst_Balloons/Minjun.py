# 못풀겠습니다 너무 어려워요 눈물납니다
# 풍선 터트릴 때 제일 작게 곱해지는 녀석을 펑 터트리고
# 다음 순회를 돌고싶은데 못하겠어요

from copy import deepcopy
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            tmp = copy.deepcopy(nums)
            tmp.del(i)
            for j in range(len(tmp)):
                hap = []
                if i == 0:
                    a = 1
                    b, c = nums[i], nums[i+1]
                elif i == len(nums)-1:
                    c = 1
                    a, b = nums[i-1], nums[i]
                else:
                    a, b, c = nums[i-1], nums[i], nums[i+1]
                hap.append(a*b*c)
        print(hap)
        return -1
            
            
