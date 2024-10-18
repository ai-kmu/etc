class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort(reverse=True)
        answer = 0
        
        for child in g:
            while s:
                candy = s.pop()
                if candy >= child:
                    answer += 1
                    break
        return answer
        
