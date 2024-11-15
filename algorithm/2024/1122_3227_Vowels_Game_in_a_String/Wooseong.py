from collections import Counter

class Solution:
    def doesAliceWin(self, s: str) -> bool:
#         # vowel 개수 세기
#         counter = Counter(s)
#         num_vowels = sum(counter[k] for k in 'aeiou')
        
#         # 사실 이 게임은 굉장히 불합리한 게임임.
#         # 모음이 없어서 Alice가 시작도 못하는 경우가 아닌 이상 무조건 이김
#         return num_vowels
    
        # 그래서 그냥 for 문 돌면서
        vowel = set('aeiou')
        for c in s:
            # aeiou가 있으면 Alice가 바로 이기는 걸로 변경
            if c in vowel:
                return True
        
        # 없으면 Bob 이김
        return False
