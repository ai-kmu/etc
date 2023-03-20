# 마지막 테스트케이스에서 time limit에 걸림 (175/176)
# 백트래킹을 사용해 해결하려고 함
# 중복되는 숫자가 엄청 많은 경우를 고려해야 함

import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # 애초에 타겟 자체를 만들수 없는 경우
        if sum(candidates) < target:
            return []
        # 같은 숫자들만 나열된 경우
        if len(set(candidates)) == 1:
            num = candidates.pop()
            if (target / num).is_integer():
                return [[num] * int(target / num)]
        n = len(candidates)
        answer = []
        visited = [False] * n
        def back(nums, res):
            # 숫자의 합이 타겟에 도달한 경우
            # answer에 정렬한 상태로 추가함(중복을 제거하기 위함)
            if res == 0:
                ans_nums = copy.deepcopy(nums)
                answer.append(sorted(ans_nums))
                return
            # 숫자의 합으로 만들 수 없는 경우 가지치기
            elif res < 0:
                return
            else:
                for i in range(n):
                    if visited[i] == True:
                        continue
                    nums.append(candidates[i])
                    visited[i] = True
                    back(nums, res - candidates[i])
                    nums.pop()
                    visited[i] = False
        
        back([], target)
        # 중복을 제거한 뒤 return
        return list(set(map(tuple, answer)))
