class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 1세기
        num_one = 0
        for i in nums:
            if i == 1:
                num_one += 1
        # 1만큼 만들기        
        temp = [1]*num_one
        # 돌면서 0이면 만들어둔 temp 왼쪽에 2면 만들어둔 temp 오른쪽에 추가
        for i in nums:
            if i == 0:
                temp.insert(0, 0)
            elif i == 2:
                temp.append(2)
            else:
                continue

        # 이거 왜 temp 로 리턴하면 안됨? 알려주셈;
        nums[:] = temp
        return nums
