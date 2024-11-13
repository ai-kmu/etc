# 답 봤습니다
class Solution:
    def rotateGrid(self, matrix: List[List[int]], rotations: int) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        
        # 레이어를 추출하는 함수
        def extract_ring(ring_num):
            ring = []
            for col in range(ring_num, cols - ring_num):  # 상단 가로
                ring.append(matrix[ring_num][col])
            for row in range(ring_num + 1, rows - ring_num):  # 오른쪽 세로
                ring.append(matrix[row][cols - ring_num - 1])
            for col in range(cols - ring_num - 2, ring_num - 1, -1):  # 하단 가로
                ring.append(matrix[rows - ring_num - 1][col])
            for row in range(rows - ring_num - 2, ring_num, -1):  # 왼쪽 세로
                ring.append(matrix[row][ring_num])
            return ring

        # 레이어를 다시 그리드에 넣는 함수
        def place_ring(ring_num, ring):
            index = 0
            for col in range(ring_num, cols - ring_num):  # 상단 가로
                matrix[ring_num][col] = ring[index]
                index += 1
            for row in range(ring_num + 1, rows - ring_num):  # 오른쪽 세로
                matrix[row][cols - ring_num - 1] = ring[index]
                index += 1
            for col in range(cols - ring_num - 2, ring_num - 1, -1):  # 하단 가로
                matrix[rows - ring_num - 1][col] = ring[index]
                index += 1
            for row in range(rows - ring_num - 2, ring_num, -1):  # 왼쪽 세로
                matrix[row][ring_num] = ring[index]
                index += 1

        # 각 레이어에 대해 rotations번 회전 후 다시 삽입
        num_rings = min(rows, cols) // 2
        for ring_num in range(num_rings):
            ring = extract_ring(ring_num)
            effective_rotations = rotations % len(ring)  # 실제 필요한 회전 수
            rotated_ring = ring[effective_rotations:] + ring[:effective_rotations]  # 회전된 링
            place_ring(ring_num, rotated_ring)

        return matrix
