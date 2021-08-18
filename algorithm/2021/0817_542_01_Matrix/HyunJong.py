class Solution:
    def updateMatrix(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # 0기준으로 bfs 사용  

        m = len(mat) ## 행
        n = len(mat[0]) ## 열

        queue = deque()
        
        ## 0이 아닌 값을 전부 무한대로 초기화
        for i, row in enumerate(mat): #행에대한
            for j, ele in enumerate(row): #열의 한 요소 값
                if ele: ## 1이면
                    mat[i][j] = float('inf') ##무한대로 초기화
                else:
                    queue.append((i, j)) ##아니면 queue에 append

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1)) ##가능한 방향 조함
        while queue: ## 초기화끝난 모든 queue에 대해
            for count in range(len(queue)): ## 
                i, j = queue.popleft() ## 제일 왼쪽부터 queue에서 값을 제거하여 확인한다.

                for x, y in directions: ## 모든 방향에 대해
                    row, col = i + x, j + y ## 이동했을 때 행렬 위치

                    if -1 < row < m and -1 < col < n and mat[row][col] > mat[i][j] + 1: ## 이동했을 때가 현재 위치보다 값이 더 큰 경우면 
                        mat[row][col] = mat[i][j] + 1 ## 값을 1 증가시켜준다.
                        queue.append((row, col)) ## 그리고 이동한 위치를 큐에 담는다.
        return mat
