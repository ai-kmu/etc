class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        valid = []

        def dfs(start_num, k, sum_num, tmp_list):
            # 조건 충족: 답안에 추가
            if k == 0 and sum_num == 0:
                valid.append(tmp_list.copy())
                return True
            # 탐색    
            for i in range(start_num, 10):
                tmp_list.append(i)
                dfs(i+1, k-1, sum_num-i, tmp_list)
                tmp_list.pop()

        # 1부터 DFS
        dfs(1, k, n, [])
        return valid
