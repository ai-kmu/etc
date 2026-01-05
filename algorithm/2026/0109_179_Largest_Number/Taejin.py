class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int("".join(sorted([str(i) for i in nums], key=lambda x: [x + x * (10 - len(x))][:10], reverse=True))))
