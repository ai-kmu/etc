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

    
    class Solution:
    def find132pattern(self, nums) -> bool:
        start_index = 0
        max_index = len(nums)
        if max_index < 3:
            return False
        min_num = nums[0]
        max_num = nums[0]
        range_arr = [[min_num, max_num]]
        range_arr_index = 0
        while True:
            try:
                start_index +=1
                if nums[start_index] > max_num:
                    max_num = nums[start_index]
                    range_arr[range_arr_index] = [min_num, max_num]
                elif nums[start_index] < min_num:
                    min_num = nums[start_index]
                    max_num = nums[start_index]
                    range_arr.append(copy.deepcopy([min_num, max_num]))
                    range_arr_index+=1
                for mi, ma in range_arr:
                    if mi < nums[start_index] < ma:
                        return True
            except IndexError:
                return False
