class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        left, right = 0, len(x)-1
        while left < right:
            if x[left] == x[right]: 
                left += 1
                right -= 1
                continue
            else: return False
        return True
