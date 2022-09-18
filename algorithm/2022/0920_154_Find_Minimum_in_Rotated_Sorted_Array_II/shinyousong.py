# 실패
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 짧은 경우
        if len(nums) <= 8:
            return min(nums)
        
        # 리스트를 복사하여 붙인다.
        nums *= 2
        # 중간에서 왼쪽에서 최초로 커지는 지점을 찾는다.
        l = len(nums)//4
        r = len(nums)//2 - 1
        term = len(nums)//8
        
        # 왼쪽이 오른쪽보다 클 때까지
        while l < r and l >= 0:
            # term은 최소 1
            if not term:
                term = 1
            # 커지는 지점에 걸리지 않은 경우 -> 바운더리를 왼쪽으로 설정
            if nums[l] <= nums[r]:
                r = l
                l -= term
                term // 2
            # 커지는 지점에 걸린 경우
            elif nums[l] > nums[r]:
                l += term
                term // 2
        return nums[l]
