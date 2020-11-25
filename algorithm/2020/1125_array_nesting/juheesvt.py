class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n=len(nums)
        dic={}
        ans=0
        for i in range(n):
            start=nums[i]
            if start in dic:
                continue
            else:
                res=1
                tmp=nums[start]
                while tmp!=start:
                    if tmp in dic:
                        res+=dic[tmp]
                        dic[start]=res
                        ans=max(ans,res)
                        break
                    else:
                        dic[tmp]=-1
                        res+=1
                        tmp=nums[tmp]
                ans=max(ans,res)
                dic[start]=res
        return ans
