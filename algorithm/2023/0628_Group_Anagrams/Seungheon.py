from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # str을 sort하여 key로 기존 str을 value로 사용

        str_dict = defaultdict(list)
        for s in strs:
            str_dict[tuple(sorted(list(s)))].append(s)

        return str_dict.values()
