class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        
        # 예외 1: s가 공백인 경우
        if not s:
            return True
        # 예외 2: s가 더 길 경우
        if len_s > len_t:
            return False
        # 예외 3: 길이가 1일 경우
        if len_s == len_t == 1:
            return s == t

        # for문은 t로 돌리고 s는 ind를 이용해서 돌림
        ind = 0
        for mother in t:
            # 같은 게 나오면 ind를 하나 늘림
            if mother == s[ind]:
                ind += 1
            # 중간에 s가 전부 커버되면 성공
            if ind == len_s:
                return True
        
        # for 문 다 돌았는데 커버 안되면 실패
        return False
