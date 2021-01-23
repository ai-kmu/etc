class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        candidate, repeated = list(), list()
        
        for i in range(len(s)-9):
            if s[i:i+10] in candidate and s[i:i+10] not in repeated:
                repeated.append(s[i:i+10])
            else:
                candidate.append(s[i:i+10])

        return set(repeated)
