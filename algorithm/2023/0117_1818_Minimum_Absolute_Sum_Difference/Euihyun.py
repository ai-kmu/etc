# 26/51 다시 풀고 있습니다.
class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
    
        temp = []
        # 돌면서 제일 작은 수 찾고
        for i in range(n):
            temp.append(abs(nums1[i]-nums2[i]))
        target = temp.index(max(temp))
        
        temp = []
        # 새로 돌면서 바꿀 숫자 찾음
        for j in range(n):
            temp.append(abs(nums2[target]-nums1[j]))
        change = temp.index(min(temp))
        
        # 바꿀 숫자로 바꾸고
        ans =0
        # 돌면서 최종합 구함
        nums1[target] = nums1[change]
        for k in range(n):
            ans += abs(nums1[k] - nums2[k])


        return ans
        
        
        
        
        
