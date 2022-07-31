# 시간 초과 

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        dq = deque()
        
        # k 가 nums의 길이와 같을 때 맥스 값 하나만 리턴
        if k == len(nums):
            return [max(nums)]
        
        # k가 1이거나 nums의 길이가 1일때 nums 바로 리턴
        if k == 1 or len(nums) == 1:
            return nums
        
        for i in range(len(nums)):
            # dq에는 nums에서의 인덱스를 넣어준다 
            # dq의 가장 마지막 인덱스 위치의 nums의 값과 현재 nums의 값을 비교해서 nums[i]의 값이 더 크면 dq에서 pop
            # nums[i]의 값보다 작은 값이 없을때까지 pop해준다 
            for j in range(len(dq)):
                if dq and nums[dq[-1]] < nums[i]:
                    dq.pop()
                else:
                    break
            dq.append(i)
            
            # 인덱스의 범위가 벗어났을 때 popleft해준다 (윈도우가 지나갔을 경우)
            if dq[0] <= i - k:   
                dq.popleft()
            
            # 윈도우 범위에서 해당하는 가장 큰 값을 append시켜준다
            if i >= k-1:
                ans.append(nums[dq[0]])
                
        return ans
