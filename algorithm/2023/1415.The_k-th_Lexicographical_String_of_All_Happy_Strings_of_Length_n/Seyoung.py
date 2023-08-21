class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        length, offset = pow(2, n - 1) * 3, k - 1
        if offset >= length:
            return ''
        
        # this is for first char of the result
        part_to_char = {0: 'a', 1: 'b', 2: 'c'}
        # this is for other chars of the result
        pre_char_to_part_char_dict = {
            'a': {0: 'b', 1: 'c'},
            'b': {0: 'a', 1: 'c'},
            'c': {0: 'a', 1: 'b'}
        }

        res = ''
        
