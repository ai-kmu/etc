# length가 4 미만 12 초과인 경우는 불가능
# 4인 경우는 unique
# 5인 경우는 leading zero 조심
# 6~12부터는 255 초과 여부도 생각해야 함...
# 그냥 재귀로 조건대로 넘기자
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def rec(s, t):
            # 남은 숫자가 부족하거나 넘치는 경우 바로 예외문자 넣음
            if len(s) > t * 3 or len(s) < t:
                return ["a"]
            # 종료조건인 경우 문제가 없으면 리턴함
            if t == 1:
                if (s[0] == "0" and len(s) >= 2) or int(s) > 255:
                    return ["a"]
                return [s]
            
            # 재귀 가능 시
            res = []
            if t > 1:
                # 문자를 한 개만 뺄 경우는 조건이 필요 없음
                temp1 = rec(s[1:], t - 1)
                for temp in temp1:
                    res.append(s[:1]+ "." + temp)
                # 문자를 두 개 이상 뺄 경우 0이 시작이면 안됨
                if s[0] != "0":
                    temp2 = rec(s[2:], t - 1)
                    for temp in temp2:
                        res.append(s[:2] + "." + temp)
                    # 문자를 세 개 뺄 경우 255가 넘으면 안됨
                    if int(s[:3]) <= 255:
                        temp3 = rec(s[3:], t - 1)
                        for temp in temp3:
                            res.append(s[:3] + "." + temp)
            return res
        # 재귀 호출
        res = rec(s, 4)
        # 오류 문자인 경우를 제거
        res = [s for s in res if "a" not in s]
        return res
            
