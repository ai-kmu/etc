class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ""
        for i in digits:
            a += str(i)
        c = int(a)+1
        d = [int(i) for i in str(c)]
        return d
