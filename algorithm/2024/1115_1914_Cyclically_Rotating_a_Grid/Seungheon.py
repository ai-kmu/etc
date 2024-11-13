
class Solution(object):
    def rotateGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        def explore(cur_i, cur_j, m, n):
            nums = []
            # 이동
            for flag, (i_di, i_dj) in enumerate([[0,1],[1,0],[0,-1],[-1,0]]): 
                range_num = n-1 if flag % 2 == 0 else m-1
                for _ in range(range_num):
                    nums.append(grid[cur_i][cur_j])
                    cur_i, cur_j = cur_i + i_di, cur_j + i_dj
                    
            return nums

        # 정답 채우기
        def fill_answer(start_i, start_j, m, n, nums, k):
            start = k
            cur_i, cur_j = start_i, start_j
            # 이동하기 전에 추가
            for flag, (i_di, i_dj) in enumerate([[0,1],[1,0],[0,-1],[-1,0]]): 
                range_num = n-1 if flag % 2 == 0 else m-1
                for _ in range(range_num):
                    # k만큼 이동해서 채우기
                    answer[cur_i][cur_j] = nums[(k + len(nums))%len(nums)]
                    cur_i, cur_j = cur_i + i_di, cur_j + i_dj
                    k += 1

        m = len(grid)
        n = len(grid[0])
        answer = [[ 0 for _ in range(n)] for _ in range(m)]
        for start_i_j in range(min(m,n)//2):
            nums = explore(start_i_j, start_i_j, m-2*start_i_j, n-2*start_i_j)
            fill_answer(start_i_j, start_i_j, m-2*start_i_j, n-2*start_i_j, nums, k)

        return answer
