class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for i in strs:
            key = "".join(sorted(i))
            if key in dict:
                dict[key].append(i)
            else:
                dict[key] = [i]
        return dict.values()
