class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        IP 주소에서 있어야 할 .(dot)은 3개
        dot이 0 이면 유효한 주소인지 확인하고 탈출
        ''' 
        
        # trivial case
        if len(s) < 4 or len(s) > 12:
            return []

        answer = []
        
        def dfs(remained_string, string, dot):
            # dot 다 썼을 때, 유효한 주소이면 추가
            if dot == 0:
                if remained_string and (int(remained_string) < 256  and not (remained_string[0] == "0" and remained_string != "0")):
                    answer.append(string + remained_string)
                return
            
            tmp = ""
            for i, c in enumerate(remained_string[:3]):
                tmp += c
                # 유효한 지 check (0~255 or 첫자리가 0인데 뒤에 숫자 붙는 경우)
                if int(tmp) > 255 or (tmp[0] == "0" and tmp != "0"):
                    break
                # 모은 숫자 넘겨서 주소 생성 반복
                string += c
                dfs(remained_string[i+1:], string+".", dot-1)
        
        dfs(s, "", 3)
        return answer
