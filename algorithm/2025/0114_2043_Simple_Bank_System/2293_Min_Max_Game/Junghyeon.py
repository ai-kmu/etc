import math


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        depth = int(math.log2(len(nums)))

        flag = True

        for d in range(depth):
            num = []
            for i in range(0, len(nums), 2):
                # print(i)
                if flag:
                    num.append(min(nums[i], nums[i+1]))
                    flag = False
                else:
                    num.append(max(nums[i], nums[i+1]))
                    flag = True
            nums = num

        return nums[0]
