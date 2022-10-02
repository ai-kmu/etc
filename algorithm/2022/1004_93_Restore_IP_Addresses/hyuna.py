class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        ans = []
        
        '''
        recursion을 통한 풀이를 구현하려고 함 
        '''
        def recursive(idx, dotcnt, ip):
            if dotcnt > 4:
                return
            if dotcnt == 4 and idx == len(s):
                ans.append(ip)
                
            
            for i in range(1, 4):
                if idx + 1 > len(s): 
                    break
               
                substr = s[idx: idx + i]
    
                if (substr[0] == "0" and len(substr) > 1) or (i == 3 and int(substr) >= 226):
                    continue
                    
                # print('idx: ', idx,'dotcnt: ', dotcnt, 'ip: ', ip+substr+("" if dotcnt==3 else "."))    
                recursive(idx+i, dotcnt+1, ip+substr+("" if dotcnt==3 else "."))

                
            
        if len(s) == 4:
            ans.append('.'.join(x for x in s))
        
        elif len(s) > 4 and len(s) <= 12:
            recursive(0, 0, '')
                
          
            
        return ans
            
