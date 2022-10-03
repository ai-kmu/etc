class Solution(object):
    def restoreIpAddresses(self, s):
        res = []
        

        def dfs(s, p, path, res):
            
            if p > 4: return
            
            if p == 4 and not s:
                res.append(path[:-1])
                return
            
            for i in range(1, len(s)+1):
                if s[:i] == '0' or (s[0] != '0' and 0 < int(s[:i]) < 256):
                    dfs(s[i:], p+1, path + s[:i]+'.', res)
                    
        dfs(s, 0, "", res)
        
        return res
    
    
    
    
