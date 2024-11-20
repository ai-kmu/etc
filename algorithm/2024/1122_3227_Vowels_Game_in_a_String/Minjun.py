# 쉽누 ㅋ

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowel = ['a', 'e', 'i', 'o', 'u']
        # 모음이 있으면 무적권 앨리스 승.
        for c in vowel:
            if c in s:
                return True
        return False
