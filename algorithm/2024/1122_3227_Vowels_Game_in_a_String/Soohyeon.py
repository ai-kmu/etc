# 만약 모음이 짝수면 Alice가 최대 홀수만큼 지우면 Bob은 못지움
# 모음이 홀수면 Alice가 다 지우면됨
# 결론적으로 Alice가 모음 하나라도 있으면 이김

class Solution(object):
    def doesAliceWin(self, s):
        
        result = 0
        vowels = ["a","e","i","o","u"]
        # 모음 갯수 세서 1개라도 있으면 True return
        for word in s:
            if word in vowels:
                result += 1

        return result >= 1