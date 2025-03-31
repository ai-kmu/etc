class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = len(str(x))
        x = str(x)
        # print(l//2)
        for i in range(l//2):
            # if i == l-i:
            #     return False
            print(x[i], x[l-i-1])
            if x[i] != x[l-i-1]:
                return False

        return True
