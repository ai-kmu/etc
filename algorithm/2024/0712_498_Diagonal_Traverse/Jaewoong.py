 class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 행렬이 비었는지 또는 첫 행이 비었는지 확인
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])  # m: 행의 수, n: 열의 수
        result = []  # 결과를 저장할 리스트
        intermediate = []  # 현재 대각선의 요소를 임시로 저장할 리스트

        # 총 대각선의 수는 m + n - 1
        for d in range(m + n - 1):
            # 새로운 대각선을 위해 intermediate 리스트 초기화
            intermediate.clear()

            # 대각선의 시작 지점 결정
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1

            # 현재 대각선의 모든 요소 수집
            while r < m and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1

            # 대각선의 인덱스가 짝수인 경우, 수집한 대각선 요소를 뒤집어서 추가
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            # 대각선의 인덱스가 홀수인 경우, 수집한 대각선 요소를 그대로 추가
            else:
                result.extend(intermediate)

        # 최종 결과 반환
        return result
