class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        index_1 = 0
        index_2 = 0
        answer = 0
        while index_1 < len(s) and index_2 < len(g):
            if s[index_1] >= g[index_2]:
                index_1 += 1
                index_2 += 1
                answer += 1
            else:
                index_2 += 1
        
        return answer
        
