class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        
        if len(s) < 4 or len(s) > 12:
            return []
        
        def validIP(depth, ip, idx, answer):
            # s를 4번 잘랐을 때, ip에 '.'을 제거한 것과 s가 동일하다면 valid한 IP
            if depth == 4:
                ip_check = ip.replace(".", "")
                if ip_check == s:
                    # valid한 IP를 answer에 append
                    answer.append(ip[:-1])
                    return
            
            # s를 길이 3으로 잘랐을 때, 그 값이 0과 255 사이 값이라면
            if idx + 3 <= len(s):
                if str(int(s[idx:idx+3])) == s[idx:idx+3] and 0 <= int(s[idx:idx+3]) <= 255:
                    # depth+1, ip에 자른 string을 더해주고, idx+3 이후를 탐색
                    validIP(depth+1, ip+s[idx:idx+3]+".", idx+3, answer)
            
            # s를 길이 2로 잘랐을 때,
            if idx + 2 <= len(s):
                if s[idx:idx+2][0] != '0':
                    validIP(depth+1, ip+s[idx:idx+2]+".", idx+2, answer)
            
            # s를 길이 1만큼 잘랐을 때,
            if idx + 1 <= len(s):
                validIP(depth+1, ip+s[idx:idx+1]+".", idx+1, answer)
            
        
        validIP(0, "", 0, answer)
        return answer
        
