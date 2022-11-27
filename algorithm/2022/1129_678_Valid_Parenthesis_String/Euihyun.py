# 테케 실패 더 풀아볼게요
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # 리스트에 채워줌
        temp = [i for i in s]
        n = len(temp)
        # 하나짜리는 바로 False
        if n == 1:
            return False
        
        # 돌면서
        while True:
            # 두개 빼고
            a = temp.pop(0)
            b = temp.pop()
            
            # 한개 남았을때 남은게 별이면 true 아니라면 false
            if len(temp) == 1:
                if temp[0] == '*':
                    return True
                return False

            # 다 나가면 true
            if len(temp) == 0:
                return True

            # 꺼낸 두개가 가능한 조합이 아니라면 false
            if a+b not in ['()', '*)', '(*', ]:
                return False

