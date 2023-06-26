class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # GroupAnagrams

        table = {}

        for i in strs:
            
            tmp = ''.join(sorted(i))
            if tmp in table:
                table[tmp].append(i)
            
            else:
                table[tmp] = [i]
        
        return list(table.values())
