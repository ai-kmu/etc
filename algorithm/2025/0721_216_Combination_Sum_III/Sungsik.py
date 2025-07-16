class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []

        # dfs로 순회
        def dfs(tmp_nums, tmp_len, tmp_sum):
            if tmp_len == k and tmp_sum == n:
                answer.append(tmp_nums)
                return
            last_num = tmp_nums[-1]
            if last_num == 9:
                return
            # 1. last_num + 1인 숫자를 추가하여 순회
            if tmp_len < k:
                dfs(tmp_nums + [last_num+1], tmp_len+1, tmp_sum+last_num+1)
            # 2. last_num에 1을 더하여 순회
            dfs(tmp_nums[:-1] + [last_num+1], tmp_len, tmp_sum+1)

        dfs([1], 1, 1)
        return answer
            
