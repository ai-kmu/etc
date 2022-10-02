class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res_IP = []
        
        def backtraking(i, dots, IP):
            # 점이 맨 끝 포함 4개일 때
            if dots == 4:
                # 마지막으로 더하고 재귀 종료
                res_IP.append(IP)
                return
            
            # i번째 수부터 3자리 앞까지 보면서
            for j in range(i, i+3):
                # 255보다 작으면
                if int(s[i:j+1]) < 255:
                    # 재귀
                    backtraking(i + 1, dots + 1, IP + s[i:j+1] + ".")
