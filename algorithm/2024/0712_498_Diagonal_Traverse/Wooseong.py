class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 크기 변수 지정
        n = len(mat)
        m = len(mat[0])

        cnt = 0  # 우상 / 좌하 방향 지정할 변수
        trav = []  # 정답
        
        # 대각선으로 탐색 == row + col값이 같은 것들끼리 탐색
        for diag in range(n + m):
            sub = []  # 현 대각선을 담아둘 리스트
            
            # 담는 건 0번 행부터 담음
            for row in range(n):
                col = diag - row  # 열의 위치는 고정
                # 인덱스 범위 고려해서 append
                if col >= 0 and col < m:
                    sub.append(mat[row][col])
                    
            # cnt에 따라서 우상 / 좌하 방향을 지정해서
            if cnt:
                trav.extend(sub)  # 그대로 넣거나
            else:
                trav.extend(sub[::-1])  # 뒤집어서 넣음
            cnt = 1 - cnt

        return trav
