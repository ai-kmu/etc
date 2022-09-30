class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        answer = []
        
        # 탐색함수
        def explore(address = [], s_pos=0):
            nonlocal answer
            
            # address가 4개가 되면, 모든 숫자를 사용했는지 확인하고 append하거나 return
            if len(address) == 4:
                if s_pos == len(s):
                    answer.append(address)
                return
            # address가 4개가 될때까지 길이를 1~3으로 슬라이스해서 이어붙이기
            # 조건에 맞지 않으면 탐색 안함
            # 조건 : 맨앞에 0이 들어가지않고, 255 이하
            else:
                for i in range(1,4):
                    if len(s) < s_pos + i:
                        break
                    tmp = address.copy()
                    split_s = s[s_pos:s_pos+i]   
                    
                    if int(split_s) > 255 or str(int(split_s)) != split_s:
                        continue
                        
                    tmp.append(split_s)
                    explore(tmp, s_pos+i)
            
        explore()

        return list(map(lambda x : '.'.join(x), answer))
