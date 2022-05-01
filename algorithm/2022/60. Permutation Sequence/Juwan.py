class Solution:
    def getPermutation(self, n: int, k: int) -> str:
    
        results = []
        prev = []
        
        num = []
    
        for i in range(n):
            
            num.append(str(i+1))
        
        
        
        def dfs(num, stop) :
            
            if stop == 0:
                
                return
            
            
            if len(num) == 0:
                
                results.append(prev[:])
                stop -= 1
                
            for e in num :
                
                next_ = num[:]
                next_.remove(e)
                prev.append(e)
                dfs(next_, stop)
                prev.pop()
            
        dfs(num, k)
        
        return ''.join(results[k-1])
