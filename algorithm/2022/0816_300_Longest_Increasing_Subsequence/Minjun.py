class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = [] 
        tmp = []
        num = 0
        for i in nums:
            if i > num:
                tmp.append(i)
                num = i
            else:
                stack.append(tmp)
                tmp = []
                num = i
                tmp.append(i)
        
        print(stack)
        print(max(len(stack)))
