class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        total = len(word)
        
        def getAnswer(i, j, num, visited):
            # 만약 순회한 횟수가 word의 길이와 같다면 True를 리턴한다
            if num == total:
                return True
            
            # 만약 올바르지 않은 위치거나
            # 이미 방문했거나
            # 알파벳이 일치하지 않는다면 False를 리턴한다.]
            if i < 0 or i == r or j < 0 or j == c or visited[i][j] or board[i][j] != word[num]:
                return False

            directions = [
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1)
            ]

            result = False
            # visited를 True로 설정한다
            visited[i][j] = True
            # 4방향에서 재귀적으로 결과값을 or연산한다
            for d in directions:
                result |= getAnswer(i+d[0], j+d[1], num+1, visited)
            # 다시 visited를 False로 바꾼다
            visited[i][j] = False
            
            return result
                        
        visited = [[False] * c for _ in range(r)]
        # 모든 노드에서 단어가 완성되는지 확인하고
        # 완성되면 True를 리턴한다
        for i in range(r):
            for j in range(c):
                if getAnswer(i, j, 0, visited):
                    return True

        return False
