class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        str_val = str(x)
        idx_left = 0
        idx_right = len(str_val) - 1
        print(idx_left, idx_right)

        while idx_left <= idx_right:
            if str_val[idx_left] == str_val[idx_right]:
                idx_left += 1
                idx_right -= 1
            else:
                return False

        return True
