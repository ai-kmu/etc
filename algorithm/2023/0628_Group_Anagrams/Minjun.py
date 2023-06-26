class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {}
        
        for s in strs:
            b = "".join(sorted(s))
            if b in a:
                a[b].append(s)
            else:
                a[b] = [s]

        return a.values()
