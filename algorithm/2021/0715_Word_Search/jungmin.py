class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0]) # board의 행과 열 크기 각각 저장
        
        def search(r,c,d): # 한 요소에서 주변 요소를 탐색하는 search 함수 정의
            # 찾는 요소 인덱스가 board범위 벗어나거나 해당 요소가 찾고자 하는 철자랑 일치 안하는 경우 함수에서 false 출력
            if r>=m or c>=n or word[d] != board[r][c] or r<0 or c<0:
                return False
            # 마지막 찾는 요소가 단어의 마지막 철자랑 같은 경우 함수에서 True 출력
            if d == len(word)-1:
                return True
            t = board[r][c] # 방문한 요소값 임시 저장
            board[r][c] = 'v' # 방문한 board 위치에 표시
            # 현재 요소에서 주변 요소 4곳 search 탐색하여 하나라도 True 만족하면 f는 True
            f = search(r+1,c,d+1) or search(r,c+1,d+1) or search(r-1,c,d+1) or search(r,c-1,d+1)
            board[r][c] = t # 방문 표시 했던 곳 다시 원래 값으로 복구
            return f # f 출력
        
        # 처음 요소부터 dfs하여 연속된 단어를 찾으면 이 함수는 True출력. 못찾으면 False 출력
        for i in range(m):
            for j in range(n):
                if search(i,j,0) : return True
                
        return False
