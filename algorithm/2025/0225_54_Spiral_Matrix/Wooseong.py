class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 길이 저장
        m = len(matrix)
        n = len(matrix[0])

        # 예외 케이스: m이나 n이 1인 애들
        if m == 1:
            # 행이 한 개 -> 첫 행 반환
            return matrix[0]
        if n == 1:
            # 열이 한 개 -> squeeze
            return [row[0] for row in matrix]

        turn = ['r', 'd', 'l', 'u']  # 오 아 왼 위 순서로 이동
        curr_turn = 0  # 현재 방향
        row = 0; col = 0  # 현재 위치
        # 초기 지점 저장 후 시작 -> 방향에 따라 이동하고 추가하는 걸로 통일하기 위함
        visited = set()
        visited.add((row, col)) # 방문한 곳 체크
        num_visited = 1  # 방문 개수 체크 -> len을 쓰면 O(n)이 지속적으로 필요하기 때문
        answer = [matrix[0][0]]  # 정답 리스트
        
        # 전부 방문 == (방문 개수 == 전체 개수)
        while num_visited < m * n:
            # 방향에 따른 각 네 가지 if 문의 구조는 동일함
            if turn[curr_turn] == 'r':
                # for 문: 방향에 맞게 이동
                for c in range(col + 1, n):
                    # 방문했던 거면 이전 스텝으로 돌아가서 for 문 종료
                    if (row, c) in visited:
                        c -= 1
                        break
                    # 방문 안했으면
                    else:
                        answer.append(matrix[row][c])  # 1) answer에 저장
                        visited.add((row, c))          # 2) visited에 추가
                        num_visited += 1               # 3) num_visited 추가
                # 끝나면 현재 위치 업데이트
                col = c
            elif turn[curr_turn] == 'd':
                for r in range(row + 1, m):
                    if (r, col) in visited:
                        r -= 1
                        break
                    else:
                        answer.append(matrix[r][col])
                        visited.add((r, col))
                        num_visited += 1
                row = r
            elif turn[curr_turn] == 'l':
                for c in range(col - 1, -1, -1):
                    if (row, c) in visited:
                        c += 1
                        break
                    else:
                        answer.append(matrix[row][c])
                        visited.add((row, c))
                        num_visited += 1
                col = c
            elif turn[curr_turn] == 'u':
                for r in range(row - 1, -1, -1):
                    if (r, col) in visited:
                        r += 1
                        break
                    else:
                        answer.append(matrix[r][col])
                        visited.add((r, col))
                        num_visited += 1
                row = r

            curr_turn = (curr_turn + 1) % 4  # curr_turn 이동
        
        return answer
