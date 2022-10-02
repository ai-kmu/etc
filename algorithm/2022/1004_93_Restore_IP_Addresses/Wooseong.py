class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def help(i, rem):
            '''
            i  : 현재 위치 (index)
            rem: 주소 네 자리 중 남은 개수
            '''
            if (rem > len(s) - i        # 뒤에 남은 스트링 개수보다 남은 주소 자리가 많거나
            or 3 * rem < len(s) - i):   # 뒤에 남은 스트링 개수가 남은 주소에 넣을 수 있는 거보다 적으면
                return                  # 중단 (backtracking)

            # 현재 위치가 끝까지 도달하면 정답
            if i == len(s):
                return answer.append(".".join(stack))

            # '0'이면 걔로 하나, 아니면 세 개 묶어서 한 자리로 해볼 거임
            k = i + 1 if s[i] == '0' else i + 3
            for j in range(i + 1, min(k, len(s)) + 1):
                # 네 자리를 묶으려 하거나
                # 255를 넘으면 패스 안됨
                if j == i + 3 and s[i:j] > "255":
                    continue
                
                stack.append(s[i:j])
                help(j, rem - 1)
                stack.pop()
        
        answer = []
        stack = []
        # 처음 위치부터 시작하고, 주소는 네 자리 남았음
        help(0, 4)
        return answer
