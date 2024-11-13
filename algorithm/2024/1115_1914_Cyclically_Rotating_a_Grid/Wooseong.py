# 정답 코드
class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        # 주소 참조 특성을 살리기 위해 함수를 내부에 정의
        def rotate(lv, rows, cols):
            # 해당 레이어에 포함된 원소 개수
            length = 2 * (rows - 1 + cols - 1)
            
            # 회전시켜야하는 수가 원소 개수의 배수면 다시 제자리임
            kk = k % length
            if kk == 0:
                return

            # 해당 레이어에 포함된 원소의 인덱스 (좌표)
            indices = [(lv + x, lv) for x in range(rows - 1)]  # 위쪽
            indices.extend((lv + rows - 1, lv + y) for y in range(cols - 1))  # 오른쪽
            indices.extend((lv + rows - 1 - x, lv + cols - 1) for x in range(rows - 1))  # 아래쪽
            indices.extend((lv, lv + cols - 1 - y) for y in range(cols - 1))  # 왼쪽

            # 회전 시켰다는 표시
            rotated = set()
            for idx, (x, y) in enumerate(indices):
                # 해당 레이어에 포함된 원소 개수와 회전 시킨 원소 개수가 같아지면 종료
                if len(rotated) == length:
                    return
                
                # 인덱스를 이용해 실제 값 가져옴
                value = grid[x][y]
                
                # 해당 좌표의 인덱스가 아직 처리되지 않았다면
                while idx not in rotated:
                    # 다음 인덱스는 회전 시켰을 때의 인덱스 == k번째 뒤의 인덱스
                    # k가 length보다 길 수 있으니까, kk를 더하고, 그래도 길 수 있으니까 나머지 구하기
                    next_idx = (idx + kk) % length
                    
                    # 그렇게 구한 인덱스로 실제 값 가져와서 치환
                    u, v = indices[next_idx]
                    value, grid[u][v] = grid[u][v], value
                    
                    # 표시하고 다음 인덱스로 지정
                    rotated.add(idx)
                    idx = next_idx

        # 가장 겉의 layer를 레벨 0이라고하면
        # 가능한 레벨은 (min(m // 2, n // 2) - 1)까지임
        for lv in range(min(m // 2, n // 2)):
            # 각 레벨 별로 가로 (col), 세로 (row) 길이 계산
            rows = m - 2 * lv
            cols = n - 2 * lv
            # 회전 - 리스트가 주소 참조라서 굳이 새로 주고 받을 필요 없음
            rotate(lv, rows, cols)
        return grid
