class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 길이만큼 회전하고 나면 더 이상 답이 없음
        n = len(s)
        cnt = 0
        while cnt < n:
            # 회전
            s = s[1:] + s[0]
            # 같아지면 True
            if s == goal:
                return True
            # 회전 횟수 추가
            cnt += 1
        # while 끝남 == 더이상 회전 못함 -> False
        return False
