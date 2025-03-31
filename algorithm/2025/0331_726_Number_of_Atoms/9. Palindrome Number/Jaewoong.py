class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_rev = reversed(str(x))
        x_revlist = []
        for j in x_rev:
            x_revlist.append(j)
        print(x_revlist)
        for i in range(len(str(x))):
            if x_revlist[i] != str(x)[i]:
                return False
                
                
        return True
