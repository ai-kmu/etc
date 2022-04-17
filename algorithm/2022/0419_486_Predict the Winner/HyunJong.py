class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 왼쪽 player와 오른쪽 player가 선택한 값 총합의 차이로 구하기.
        # 두 차이중 중에 최대 값을 기준으로 선택하면 된다.
        # 음수가 나오면 패배, 양수가 나오면 승리
        def choice(nums, l, r):
            if (l == r): # 종료 조건
                return nums[l]
            
            left_start = nums[l] - choice(nums, l+ 1, r) # player가 왼쪽을 선택
            right_start = nums[r] - choice(nums, l, r - 1) # player가 오른쪽을 선택
            return max(left_start, right_start) # 둘 중에 큰값을 return
            
        diff_num = choice(nums, 0, len(nums)-1) 
        aws =  (diff_num>=0) # 총합이 0보다 크면 player 1 승리
        return aws
