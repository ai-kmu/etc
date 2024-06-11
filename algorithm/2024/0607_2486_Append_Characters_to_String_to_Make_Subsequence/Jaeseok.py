class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        # 만약 이미 t가 s의 subsequence라면 답은 0
        if t in s:
            return 0
        
        # s를 순회하면서 t가 순서대로 s에 얼마나 들어있는지 확인
        cur = 0
        for i in s:
            # 만약 현재 t에 있는 알파벳이 s에 있다면 다음 알파벳 확인
            if t[cur] == i:
                cur += 1
        
        # 순서대로 들어있지 않은 나머지는 전부 새로 append해야하므로 그 차이를 return
        return len(t) - cur
      
