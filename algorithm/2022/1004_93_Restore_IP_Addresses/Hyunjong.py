class Solution(object):
    def restoreIpAddresses(self, s):
        answer = []

        def dfs(ip, left, cnt):
            # 종료 조건
            if cnt == 4:
                if not left:
                    if ip not in answer:
                        answer.append(ip)
                return

            elif not left:
                return
            
            # 처리 시작
            # 시작 정수가 0인 경우
            if left[0] == '0':
                if cnt == 3:
                    ip += '0'
                else:
                    ip += '0.'
                dfs(ip, left[1:], cnt+1)
            
            # 0이 아닌 경우
            else:
                ip_1 = left[:1]
                ip_2 = left[:2]
                ip_3 = left[:3]
                if cnt != 3:
                    ip_1 += '.'
                    ip_2 += '.'
                    ip_3 += '.'

                # 1개, 2개, 3개 정수로 나눠서 탐색 시작
                dfs(ip+ip_1, left[1:], cnt+1)
                dfs(ip+ip_2, left[2:], cnt+1)
                # 3개인 경우 255보다 작아야 함
                if int(left[:3]) <= 255:
                    dfs(ip+ip_3, left[3:], cnt+1)

        dfs('', s, 0)
        return answer
