from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)
        
        for st in strs:
            # string을 key 형태로 바꾸기 위해
            # sorting하고 tuple로 변환
            word_dict[tuple(sorted(st))].append(st)
        
        return word_dict.values()
