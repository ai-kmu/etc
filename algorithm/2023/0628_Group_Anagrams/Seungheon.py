from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 등장하는 str을 카운트해서 dictionary의 key값으로 사용
        # value는 str

        str_dict = defaultdict(list)
        for s in strs:
            key = [0]*26
            for c in s:
                key[ord(c)-97] += 1
            str_dict[tuple(key)].append(s)

        return str_dict.values()
