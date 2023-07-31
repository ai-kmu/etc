class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking 사용
        # 시작, 타겟, path설정
        def backtrack(start, target, path):
            # 만약 타겟이 0보다 작으면 그대로 반환
            if target < 0:
                return

            # 만약 타겟이 0이면 현재 만든 path를 더한 후 반환
            if target == 0:
                result.append(path)
                return

            # 처음 시작부터 candidate를 돌며 backtracking 수행
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])

        # 처음 path를 빈 리스트로 설정한 후에 처음 시작은 0, 타겟은 target으로 시작
        result = []
        backtrack(0, target, [])
        return result
