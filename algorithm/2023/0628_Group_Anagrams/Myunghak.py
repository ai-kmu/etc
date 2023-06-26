# default dict를 이용하여 key에는 문자열을 sorting한값, value에는 sorting되기 전 값을 집어 넣는다.
# 그럼 같은 key값을 가진 값에는 같은 문자로 이루어진 값끼리 모이게 된다.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ddict = defaultdict(list)
        
        for word in strs:
            ddict["".join(sorted(word))].append(word)
        
        return ddict.values()
