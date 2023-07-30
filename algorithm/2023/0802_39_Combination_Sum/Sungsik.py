from collections import defaultdict

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = set()
        # key는 남은 숫자, value는 지금까지의 조합들의 set
        combs = defaultdict(set)
        # 기본 값으로 남은 숫자는 target, 조합을 빈 tuple로 만듦
        combs[target].add(())
        
        for c in candidates:
            new_combs = combs.copy()
            for remained, tmp_combs in combs.items():
                for tmp_comb in tmp_combs:
                    new_remained = remained
                    new_comb = list(tmp_comb)
                    # 남은 숫자가 현재 숫자보다 클 경우
                    while new_remained >= c:
                        # 이를 빼고 조합에 추가한다
                        new_remained -= c
                        new_comb.append(c)
                        # 만약 남은 숫자가 0일 경우 answer에 추가
                        if new_remained == 0:
                            answer.add(tuple(new_comb))
                        # 아닐 경우 combs에 추가
                        else:
                            new_combs[new_remained].add(tuple(new_comb))
            combs = new_combs
        
        return list(answer)
