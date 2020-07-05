import collections

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
            
        deque = collections.deque()                          # 스택으로 사용할 deque
        mins = [0 for _ in range(len(nums))]                 # mins 배열 생성 (현 위치까지 가장 작은 수를 뜻함)
        mins[0] = nums[0]
        for i in range(1,len(nums)):                         
            mins[i] = min(mins[i-1], nums[i])
        for j in range(len(nums)-1, -1, -1):                 # 역순
            if nums[j] > mins[j]:                            # nums[j]가 mins[j]보다 큰 경우  (1<3)
                while len(deque)>0 and deque[-1] <= mins[j]: # 스택 top이 mins[j] 이하면 pop (2<=3) 
                    deque.pop()
                if len(deque)>0 and deque[-1] < nums[j]:     # 스택 top이 nums[j]보다 작으면 조건 성립 (1<3<2)
                    return True
                deque.append(nums[j])                        # 아니면 스택에 nums[j] push
        return False
