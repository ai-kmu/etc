class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # row의 방향
        direction = [1, -1, 0]
        # 현재 방향
        curr_dir = direction[0]
        # 현재 row 위치
        curr_row = 0
        # temporal answer 초기화
        temp_answer = ['' for _ in range(numRows)]
        
        for char in s:
            # 만약 numRow가 1이면 쭉 이어 붙이기
            if numRows == 1:
                temp_answer[0] += char
                continue
            elif curr_row == 0: # 첫번째 row라면 밑으로 내려가야됨.
                curr_dir = direction[0]
            elif curr_row == numRows-1: # 마지막 row라면 올라가야됨.
                curr_dir = direction[1]
            temp_answer[curr_row] += char # 현재 row에 character 추가
            curr_row += curr_dir # 현재 row 업데이트
        
        # list to string
        return ''.join(temp_answer)
