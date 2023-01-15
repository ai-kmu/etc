class Solution:
    def minAbsoluteSumDiff(self, nums1, nums2):
        sorted_num1 = sorted(nums1)

        def closest_number(L, k):
            left, right = 0, len(L) - 1
            closest = None
            closest_diff = None
            while left <= right:
                mid = (left + right) // 2
                diff = abs(L[mid] - k)
                if closest is None or diff < closest_diff:
                    closest = L[mid]
                    closest_diff = diff
                if L[mid] < k:
                    left = mid + 1
                elif L[mid] > k:
                    right = mid - 1
                else:
                    return L[mid]
            return closest


        def bst(num):
            l, r = 0, len(nums1) - 1
            while(l+1 <= r):
                if abs(sorted_num1[l] - num) > abs(sorted_num1[r] - num):
                    l = l + 1
                elif sorted_num1[r] > num:
                    r = r - 1
                
            if l < len(nums1):
                return sorted_num1[l] if abs(sorted_num1[l] - num) < abs(sorted_num1[r] - num) else sorted_num1[r]
            else:
                return sorted_num1[r]
            
        max_n = -1
        answer = 0
        for i in range(len(nums1)):
            answer += abs(nums1[i] - nums2[i])
            N = abs(nums1[i] - nums2[i]) - abs(closest_number(sorted_num1,nums2[i]) - nums2[i])
            if N > max_n:
                max_n = N
        
        print(answer, max_n)
        return (answer - max_n) % (10**9+7)
