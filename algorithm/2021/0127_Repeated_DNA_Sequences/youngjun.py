class Solution(object):
    def findRepeatedDnaSequences(self, s):
        ans = set()
        seen = set()

        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            if seq in seen:
                ans.add(seq)
            seen.add(seq)

        return list(ans)
        
