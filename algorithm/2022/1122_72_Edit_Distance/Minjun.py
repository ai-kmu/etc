# dp로 풀어보려했지만 못 풀겠음
# 해당 코드는 순서대로 비교하면서 같은 애 카운트하는 코드
# 정방향이나 역방향이나, 중복 글자가 있으면 카운트 망가짐,, 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def Wlw(c, lis):
            nonlocal cnt
            for i, s in enumerate(lis):
                if c == s:
                    cnt += 1
                    return lis[i+1:]
                
            return lis
        cnt = 0
        
        nw = word2
        
        for a in word1:
            
            nw = Wlw(a, nw)
        
        l1 = len(word1)
        l2 = len(word2)

        if l1 > l2:
            return l1-cnt
        else:
            return l2-cnt
