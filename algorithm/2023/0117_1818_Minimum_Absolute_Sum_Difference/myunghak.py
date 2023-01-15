class Solution:
    def minAbsoluteSumDiff(self, nums1, nums2):
        sorted_num1 = sorted(nums1)
        def bst(num):
            l, r = 0, len(nums1) - 1
            while(l <= r):
                mid = (l + r) // 2

                if sorted_num1[mid] < num:
                    l = mid + 1
                elif sorted_num1[mid] > num:
                    r = mid - 1
                else:
                    return sorted_num1[mid]
                
            if l < len(nums1):
                return sorted_num1[l] if abs(sorted_num1[l] - num) < abs(sorted_num1[r] - num) else sorted_num1[r]
            else:
                return sorted_num1[r]
            
        max_n = -1
        answer = 0
        for i in range(len(nums1)):
            answer += abs(nums1[i] - nums2[i])
            N = abs(nums1[i] - nums2[i]) - abs(bst(nums2[i]) - nums2[i])
            if N > max_n:
                max_n = N
        
        print(answer, max_n)
        return answer - max_n
