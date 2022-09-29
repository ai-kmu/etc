class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 길이가 4 미만, 12 초과면 불가능
        if len(s) < 4 or len(s) > 12:
            return []
        
        answer = []
        
        # s의 일부분이 숫자로 변화할수 없거나, 0~255범위가 아니거나, 0으로 시작할 경우
        # return false
        def valid_check(sub_s):
            try:
                num = int(sub_s)
                if not 0 <= num <= 255 or str(num) != sub_s:
                    return False
                return True
            except ValueError:
                return False
        
        def dfs(start, n, new_s):
            # .을 3개 찍었을 경우
            # 마지막 부분만 체크해서 가능하면 answer에 넣고 아니면 넣지 않는다.
            if n >= 3:
                if valid_check(s[start:]):
                    answer.append(new_s+s[start:])
            else:
                # 숫자를 1개부터 3개 사용 가능
                for end in range(start+1, start+4):
                    sub_s = s[start:end]
                    # 만약 해당 숫자를 사용할 수 있을 경우
                    # new_s에 .을 붙인 후 sub_s를 추가한 후
                    # dfs를 수행
                    if valid_check(sub_s):
                        old_s = new_s
                        new_s += sub_s + "."
                        dfs(end, n+1, new_s)
                        new_s = old_s
        
        dfs(0, 0, "")
        return answer
