class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = 0
        # pivot 찾은 다음 원래대로 정렬한다.
        # O(n)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                nums = nums[i+1:] + nums[:i+1]
                pivot = i + 1
                break
        
        # binary search
        # O(logn)
        start, end = 0, n-1
        while start <= end:
            mid = start + ((end - start) // 2)
            if nums[mid] == target:
                # 기존 index를 return 해야 하기 때문에
                # pivot만큼 더하고 n으로 나눈 나머지를 리턴한다.
                return (mid + pivot) % n
            elif target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return -1
