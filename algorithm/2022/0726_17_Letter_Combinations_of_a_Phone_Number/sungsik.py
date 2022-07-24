from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    
        # 조합할 letter를 찾음
        all_letters = [digit_to_letter[digit] for digit in digits]
        
        # itertools.product를 활용해 모든 경우의 수를 조합
        return ["".join(letters) for letters in product(*all_letters)]
