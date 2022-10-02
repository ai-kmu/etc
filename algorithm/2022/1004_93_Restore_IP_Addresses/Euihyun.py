# dfs 로 풀수 있을거란 생각은 했지만 구현을 못함..
# 거의 구현을 못했기 때문에 그대로 내기보단 정답코드를 찾아보고 python Tutor로 로직 살펴보면서 공부함
# 정답을 본 코드 여서 코드리뷰는 안해주셔도 될거같습니다.

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        ans = []
        temp = []
        # 0.0.0.0 ~ 255.255.255.255 가 아닐경우 리턴
        if len(s) < 4 or len(s) > 12:
            return ans
        
        # dfs 돌면서 가능한것들 탐색하고 추가
        def dfs (now, end):
            # 끝까지 가서 len(s) 만큼 채웠다면 조건을 만족 한거기 때문에 ans에 추가
            if end == 0:
                if now == len(s):
                    ans.append('.'.join(temp[:]))
                    return
                return
            
            # 숫자 하나씩 보면서 조건에 맞다면 추가
            for i in range(now, len(s)):
                digit = s[now:i+1]
                # 0으로 시작하면서 2자리수 이상이거나 또는 숫자가 255를 넘으면 return
                if (digit[0] == "0" and len(digit) > 1 ) or (int(digit) > 255):
                    return
                # 아닌경우 temp에 추가하고 다시 dfs 돌면서 탐색 
                temp.append(digit)
                dfs(i+1, end-1)
                # 4번 돌았으면 pop 됨
                temp.pop()
        dfs(0,4)
        return ans
