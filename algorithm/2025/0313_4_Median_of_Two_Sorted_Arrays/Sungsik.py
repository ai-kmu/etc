class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(log(m+n))으로 풀려다가 도저히 안되겠어서 O(m+n)으로 풀어보았습니다.
        # 방법은 그냥 간단히 total_nums에 nums1과 nums2를 merge하고 median을 구하는 방식으로 풀었습니다.
        total_nums = []
        
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        
        while i < m or j < n:
            if not i < m:
                total_nums += nums2[j:]
                break
            if not j < n:
                total_nums += nums1[i:]
                break
            
            n1, n2 = nums1[i], nums2[j]
            
            if n1 < n2:
                total_nums.append(n1)
                i += 1
            elif n1 > n2:
                total_nums.append(n2)
                j += 1
            else:
                total_nums.append(n1)
                total_nums.append(n2)
                i += 1
                j += 1
        
        total_len = len(total_nums)
        
        return total_nums[total_len//2] if total_len % 2 == 1 else (total_nums[total_len//2-1] + total_nums[total_len//2]) / 2
            
