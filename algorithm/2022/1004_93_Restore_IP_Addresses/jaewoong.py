# 풀이실패...
# 늦게올려서 죄송합니다...
# 막혔다가 다시풀어야지 했다가 쌔까맣게 잊어버렸습니다...
# 다시봐도 모르겠네요...
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []      
        string = ''
        now = ''
        n = 0 
        for r in s:            
            if n == 3:
                string += now
                string += '.'
                now = ''
                n = 0
                
            n += 1
            if int(now + r) <= 255:
                now += r
            elif int(now + r) > 255:
                now += '.'
                now += r
            else:
                string+=now
        print(string)
