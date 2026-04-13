# 문제 지시대로 빡 구현했음. 특별한 알고리즘없음.
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            flag = True
            a = nums[l[i]:r[i]+1]
            a.sort()
            for j in range(1,len(a)):
                if a[j]-a[j-1] != a[1]-a[0]:
                    flag = False
            if flag:
                ans.append(flag)
            else:
                ans.append(flag)
        return ans
