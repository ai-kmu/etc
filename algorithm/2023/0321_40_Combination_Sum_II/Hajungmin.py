class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        # 요소 중 target보다 큰 값을 제외
        for i in candidates[::-1]:
            if i <= target:
                break
            candidates.pop()

        ans = []
        
        # target보다 작은 수들만 있는 리스트로 DFS수행
        def dfs(combi, idx, target):

            # 만약 target 값이 0이 되면 리스트 안의 합이 target과
            # 동일하기 때문에 ans에 조합을 더해줌
            if target == 0:
                ans.append(combi[:])
                return
            
            # 먼저 이전 값을 prev_num으로 설정
            # candidates에는 음수가 없기 때문에 -1로 설정
            prev_num = -1
            for i in range(idx, len(candidates)):
                # prev_num과 현재 값이 같다면 중복이기 때문에 continue
                if candidates[i] == prev_num:
                    continue

                if target - candidates[i] < 0:
                    break

                # 현재 숫자와 이전 숫자가 같지 않고 
                # 현재 target에서 candidates의 현재 값을 뺏을 때 
                # 음수가 아닌 경우 조합 결과에 현재 수를 더한 다음
                # dfs에 넣어준다 이 때 target은 현재 값을 빼준 값으로 넣어준다
                combi.append(candidates[i])
                dfs(combi, i+1, target-candidates[i])

                # dfs가 끝난 후에 pop을 통해 combi를 비워줌
                combi.pop()

                # prev_num을 candidates의 현재 숫자로 업데이트
                prev_num = candidates[i]

        # dfs 수행
        dfs([], 0, target)

        return ans
