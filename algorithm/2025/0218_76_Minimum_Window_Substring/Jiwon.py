# 솔루션 참고

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # substring 성립 불가
        if len(s) < len(t):
            return ""
        
        needstr = Counter(t)
        needcnt = len(t)
        res = (0, float('inf'))
        start = 0

        # 윈도우 크기 키워가며 문자 포함 확인
        for end, ch in enumerate(s):
            if needstr[ch] > 0:
                needcnt -= 1
            needstr[ch] -= 1
            # 필요 문자(t)를 전부 포함한 경우 최소 윈도우 갱신
            if needcnt == 0:
                while True:
                    tmp = s[start]
                    if needstr[tmp] == 0:
                        break
                    needstr[tmp] += 1
                    start += 1
                if end - start < res[1] - res[0]:
                    res = (start, end)
                needstr[s[start]] += 1
                needcnt += 1
                start += 1
                
        return '' if res[1] > len(s) else s[res[0]:res[1]+1]
