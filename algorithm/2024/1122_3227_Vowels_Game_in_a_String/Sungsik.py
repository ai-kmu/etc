class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # Alice가 있는 필승법이 있을 것 같다.
        # 그래서 모음이 하나라도 없는 경우를 제외하고 True를 리턴했더니 풀렸다.
        vowels = set(['a','i','e','o','u'])
        for c in s:
            if c in vowels:
                return True
        return False
                
