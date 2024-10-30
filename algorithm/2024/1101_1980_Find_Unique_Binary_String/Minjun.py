# 풀이 참고했습니다..
# 리뷰 안해주셔도 됩니다
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        s= s et(int(x,2) for x in nums)
        def pod(x,n):
            n1 = len(x)
            return ("0"*(n-n1))+x
        for x in range(1<<n):
            if x not in s:
                return pod(bin(x)[2:],n)
        return "0" * n       
