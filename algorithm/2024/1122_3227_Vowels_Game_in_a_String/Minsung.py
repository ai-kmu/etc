class Solution:
    def doesAliceWin(self, s: str) -> bool:
        self.is_vowel = dict()  # key: alpha, value: bool
        for alpha in range(ord('a'), ord('z')+1):
            if chr(alpha) in ['a', 'e', 'i', 'o', 'u']:
                self.is_vowel[chr(alpha)] = True
            else:
                self.is_vowel[chr(alpha)] = False
        
        while True:
            last_index = self.Alice_turn(s)
            if last_index is None:
                return False
            s = s[last_index+1:]
            last_index = self.Bob_turn(s)
            if last_index is None:
                return True
            s = s[last_index+1:]
    
    def Alice_turn(self, s:str) -> str:
        vowel_counter = 0
        last_index = None  # 삭제할 수 있는 최대 index
        for i, ch in enumerate(s):
            if self.is_vowel[ch]: 
                vowel_counter += 1
                if vowel_counter%2 != 0:
                    last_index = i
        return last_index
    
    def Bob_turn(self, s:str) -> str:
        vowel_counter = 0
        last_index = None  # 삭제할 수 있는 최대 index
        for i, ch in enumerate(s):
            if self.is_vowel[ch]: 
                vowel_counter += 1
                if vowel_counter%2 == 0:
                    last_index = i
        return last_index
