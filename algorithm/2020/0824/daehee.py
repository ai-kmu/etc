class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        
        strings = ['' for _ in range(numRows)]                  # 라인별로 선언
        strings_idx = 0                                         # for문에서 사용할 strings index
        down = False                                            # idx 이동시킬 방향
        
        for c in s:
            strings[strings_idx] += c                           # 해당 라인에 더해주기
            if strings_idx==0 or strings_idx==numRows-1:        # 끝부분일 경우 방향 바꿈
                down = not down                                
            strings_idx += 1 if down else -1                    # 방향으로 1칸 변경
                
        result = ''
        for row in strings:
            result += row
            
        return result
