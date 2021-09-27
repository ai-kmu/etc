class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pivot을 찾아주는 함수
        # O(logn)
        def find_pivot(start, end):
            while start <= end:
                mid = start + ((end - start) // 2)
                if mid < end and nums[mid] > nums[mid + 1]:
                    return mid + 1
                elif mid > start and nums[mid] < nums[mid - 1]:
                    return mid
                elif nums[mid] > nums[start]:
                    start = mid + 1
                else:
                    end = mid - 1
            return start + 1
        
        n = len(nums)
        start, end = 0, n-1
        pivot = 0
        # 만약 제일 앞의 값이 제일 뒤의 값보다 클 경우
        # rotated 되었다고 판단하고 pivot을 찾은 후 원래대로 정렬한다
        if nums[start] > nums[end]:
            pivot = find_pivot(start, end)
            nums = nums[pivot:] + nums[:pivot]

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
