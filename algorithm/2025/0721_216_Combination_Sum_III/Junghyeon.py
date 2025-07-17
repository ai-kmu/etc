# DFS
class Solution(object):
    def combinationSum3(self, k, n):
        def dfs(curr_num, path):
            if len(path) == k:
                if sum(path) == n:
                    result.append(list(path))
                return
                
            for num in range(curr_num, 10):
                path.append(num)
                dfs(num + 1, path)
                path.pop()

        result = []
        dfs(1, [])

        return result
