class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels =['a', 'e', 'i', 'o', 'u']

        for i in vowels:
            if i in s:
                return True
            
        return False
