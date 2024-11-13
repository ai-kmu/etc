# 계속 틀려서 답지 봤습니다 ㅠ
class Solution(object):
    def rotateGrid(self, grid, k):
        m, n = len(grid), len(grid[0])
        # 레이어마다 한바퀴 도는 함수 
        def rotate(top,bot,left,right):
            # 처음 왼쪽 위 값 저장
            tmp = grid[top][left]
            # 위 아래 왼쪽 오른쪽 돌리면서 값 변환
            for i in range(left,right):    grid[top][i]   = grid[top][i+1]
            for i in range(top,bot):       grid[i][right] = grid[i+1][right]
            for i in range(right,left,-1): grid[bot][i]   = grid[bot][i-1]
            for i in range(bot,top,-1):    grid[i][left]  = grid[i-1][left]
            # 처음 왼쪽 위 값 다음 자리로 반환 
            grid[top+1][left] = tmp
        # 작은 변 길이의 // 2는 cycle 수
        for i in range(min(m,n)//2):
            # k가 현재 cycle의 요소 수 보다 크면 헛도는게 됨
            # 헛도는거 만큼 제거하기
            kk = k%(2*(m+n-4*i-2))
            for _ in range(kk): 
                rotate(i, m-i-1, i, n-i-1)
        return grid
