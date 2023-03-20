class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        # 오름차순으로 정렬
        candidates.sort()
        # print(candidates)
        answer = []

        # lru_cache를이용하여 dp개념 이용
        @lru_cache(None)
        def explore(idx = -1, cur = 0, tmp_cand = ()):
            # idx의 뒤의 수부터 탐색
            for i in range(idx+1, len(candidates)):
                # print(idx, cur, tmp_cand, i)
                # 아직 target 보다 작다면
                if cur + candidates[i] < target:
                    tmp = list(explore(i, cur + candidates[i], tuple(list(tmp_cand) + [candidates[i]])))
                    if tmp and not tmp in answer:
                        answer.append(tmp)
                # target 값과 같다면
                elif cur + candidates[i] == target:
                    tmp = list(tmp_cand) + [candidates[i]]
                    if idx == -1 and not tmp in answer:
                        answer.append(tmp)
                        break
                    return tuple(list(tmp_cand) + [candidates[i]])
                # target 값보다 크다면
                else:
                    break

            return ()
            
        explore()

        return answer
