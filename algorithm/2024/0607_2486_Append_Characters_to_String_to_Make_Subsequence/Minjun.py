class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_len = len(s)
        t_len = len(t)

        # s가 포함하는 t prefix idx 표시용
        fivot = -1
        # s가 포함하는 t 길이 표시용 
        idx = -10000
        # s에 포함되는 최대한 긴 t prefix 찾기
        for i, _ in enumerate(t):
            tmp = s.find(_)
            # 탈출: s에 t가 없으면 멈춤 -> return t_len - i => 나머지 모두 append 되어야함
            if tmp == -1:
                idx = i
                break

            # 포함되면 기록
            fivot = tmp

            # s를 모두 순회했으면 멈춤 -> return t_len - i => 나머지 모두 append 되어야함
            if fivot == s_len:
                idx = i
                break
            
            # prefix 순서 유지를 찾은 t 위치 이전 s는 제거
            s = s[fivot+1:]
        
        # idx가 갱신 안됐으면 추가할 append가 없는 것 (포함관계)
        if idx == -10000:
            return 0
        return t_len - idx
