class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: # nums가 비어있는 경우 0 리턴
            return 0
        
        if len(nums) == 1:  # nums의 길이가 1인 경우 그 요소를 리턴
            return nums[0]
        
        if len(nums) == 2: # nums의 길이가 2인 경우 둘 중 최대값을 리턴
            return max(nums[0],nums[1])
        
        stack = [0] * len(nums) # 규칙대로 nums안 요소 더했을 때 최댓값을 넣는 변수 선언
        stack[0] = nums[0] # stack의 첫번째 요소는 nums의 첫번째 요소
        stack[1] = max(nums[0], nums[1]) # stack의 두번째 요소는 nums[0]과 nums[1] 중 최댓값 선택
        
        for i in range(2, len(nums)): # stack의 이전값과 그 이전값과 현재 인덱스에 해당하는 nums의 값을 더했을 때 둘 중 최댓값을 선정해 stack에 저장
            # 이러한 형식으로 stack에 값을 넣다 보면 stack의 마지막 값은 결국 규칙에 따른 nums안 요소합의 최댓값을 출력시킬 수 있음.
            stack[i] = max(stack[i-1], stack[i-2] + nums[i])
                
        return stack[-1]
