class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 집이 하나인 경우 ex) [1]
        if n == 1:
            return nums[0]
        # 첫번째집과 마지막집이 연결된 구조이므로 아래와같이 두 경우가 존재
        # nums1 = 첫번째 집부터 털 경우(마지막 집 불가능)
        # nums2 = 두번째 집부터 털 경우(마지막 집 가능)
        nums1 = [0]*2 + nums[:len(nums)-1]
        nums2 = [0]*2 + nums[1:]
        mx = 0
        for i in range(2, len(nums1)):
            mx = max(nums1[i-2], mx)
            nums1[i] += mx
        
        mx = 0
        for i in range(2, len(nums2)):
            mx = max(nums2[i-2], mx)
            nums2[i] += mx
        # 첫번째집부터 턴 경우와 두번째집부터 턴 경우중 더 큰 값을 return
        return max(nums1 + nums2)
