# 풀이 참고해서 풀었습니다. 리뷰 안해주셔도 됩니다..

class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0]) # 크기 저장 
        
        for l in range(min(m, n) // 2): # 레이어만큼 순회 돌리기
            i = j = l
            l_to_arr = []
            # 레이어별 4가지 방향을 분리해서 하나의 어레이로 표현
            for r in range(j, n - j - 1):     l_to_arr.append(grid[i][r]) # 오른쪽
            for d in range(i, m - i - 1):     l_to_arr.append(grid[d][n - j - 1]) # 아래쪽
            for l in range(n - j - 1, j, -1): l_to_arr.append(grid[m - i - 1][l]) # 왼쪽
            for u in range(m - i - 1, i, -1): l_to_arr.append(grid[u][j]) # 위쪽
                
            kk = k % len(l_to_arr) # 변수 길이 보다 크면 순환이 같아지므로 모듈러
            l_to_arr = l_to_arr[kk:] + l_to_arr[:kk] # 순환
            
            # 다시 4가지 방향으로 분리해서 하나의 순환된 어레이를 레이어별 그리드로 변환
            x = 0  
            for r in range(j, n - j - 1):     grid[i][r] = l_to_arr[x]; x += 1 # 오른쪽
            for d in range(i, m - i - 1):     grid[d][n - j - 1] = l_to_arr[x]; x += 1 # 아래쪽
            for l in range(n - j - 1, j, -1): grid[m - i - 1][l] = l_to_arr[x]; x += 1 # 왼쪽
            for u in range(m - i - 1, i, -1): grid[u][j] = l_to_arr[x]; x += 1 # 위쪽

        return grid
