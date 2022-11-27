class Solution(object):
    def checkValidString(self, s):

        cnt = 0
        star = 0
        
        for c in s:
            
            if c == '(':
                cnt += 1
            elif c == '*':
                star += 1
            else:
                if cnt > 0:
                    cnt -= 1
                elif cnt == 0 and star > 0:
                    star -= 1
                else:
                    return False
        
        while cnt > 0 and star > 0:
            cnt -=1
            star -= 1
                
        return cnt == 0
