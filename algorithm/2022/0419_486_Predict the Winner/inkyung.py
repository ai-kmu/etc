class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def dfs(visited, nums):
            tu_nums = tuple(nums)
            if tu_nums in visited:
                return visited[tu_nums]
            if len(nums) == 1:
                return nums[0]
            # 시작을 골랐을 때, 마지막을 골랐을 때 모두를 비교해서 최대값을 뽑도록 설정
            # -> 최대값을 뽑도록 했음에도 0보다 작아지면 절대 이길 수 없는 것
            score = max(nums[0] - dfs(visited, nums[1:]), nums[-1] - dfs(visited, nums[:-1]))
            visited[tu_nums] = score
            return score
        visited = {}
        return True if dfs(visited, nums) >= 0 else False
