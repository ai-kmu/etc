# 실패하고 답 봤습니다. 리뷰 안해주셔도 돼요

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows, cols = len(board), len(board[0])

        # 재귀
        def search(row, col, index):
            # 단어의 모든 문자를 찾았을 때
            if index == len(word):
                return True

            # 보드 범위를 벗어나거나 현재 셀의 문자가 일치하지 않는 경우
            if (row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[index]):
                return False

            # 현재 셀을 일시적으로 표시하여 다시 방문하지않음
            temp, board[row][col] = board[row][col], "*"

            # 상하좌우 인접 셀로 이동하면서 다음 문자를 찾음
            find = (
                search(row + 1, col, index + 1)
                or search(row - 1, col, index + 1)
                or search(row, col + 1, index + 1)
                or search(row, col - 1, index + 1)
            )

            # 탐색이 끝나면 현재 셀을 원래대로 복원
            board[row][col] = temp

            return find

        # 보드의 모든 셀에서 시작하여 단어를 찾음
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if search(row, col, 0):
                        return True

        return False

        
