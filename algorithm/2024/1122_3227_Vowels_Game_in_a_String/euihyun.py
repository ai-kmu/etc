# 모음 있으면 무족건 이기는 엘리스~

class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 문자 중에 모음 있으면 엘리스가 이김
        for i in s:
            if i in 'aeiou':
                return True

        return False
