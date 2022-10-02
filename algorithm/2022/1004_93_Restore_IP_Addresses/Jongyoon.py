class Solution(object):
    def restoreIpAddresses(self, s: str) -> List[str]:
    
        result = []
        
        if len(s) < 4 or len(s) > 12:                                                          # 최소 길이 : 4, 최대 길이 : 12 
            return None
        
        for a1 in range(1, 4):               
            for a2 in range(1, 4):
                for a3 in range(1, 4):
                    for a4 in range(1, 4):
                        if len(s) == a1 + a2 + a3 + a4:                                        # array에서 선택할 원소의 수가 전체 원소와 같아야 함.
                            
                            first = s[0:a1]                                                    # 첫 번째 ip
                            second = s[a1:a1+a2]                                               # 두 번째 ip 
                            third = s[a1+a2:a1+a2+a3]                                          # 세 번째 ip
                            fourth = s[a1+a2+a3:a1+a2+a3+a4]                                   # 네 번째 ip
                                                        
                            data = list(map(self.CheckNum, [first, second, third, fourth]))    # check invalid ip 
                            
                            if None not in data:                                               # check 후 문제가 없다면  
                                result.append(".".join(data))                                  # . 으로 나눈 후 join
                    
        return result
    
    # 첫 번째 숫자가 0 or 255 보다 큰 경우 check
    def CheckNum(self, num):
        if (len(num) > 1 and num[0] == "0") or int(num) > 255 :
            return None
        return num
    
    
           
            
