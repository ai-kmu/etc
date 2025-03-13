class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in str(int("".join([str(d) for d in digits])) + 1)]
