class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        rv_str_x = ''
        for i in range(len(str_x)-1, -1, -1):
            rv_str_x += str_x[i]
        return rv_str_x == str_x
