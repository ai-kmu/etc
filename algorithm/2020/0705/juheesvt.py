class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        # 입력된 리스트의 길이가 2이하이면 False !
        if len(nums) <=2:
            return False

        third = float('-inf')
        stack = []
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < third:
                return True
            else:
                
                #stack의 top이 num[i]보다 작으면 pop !
                while stack and stack[-1] < nums[i]:
                    third = stack.pop()
            stack.append(nums[i])
        return False
