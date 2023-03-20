class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # brute-force로 풀면 time-error 발생
        
        if not candidates:
            return []
        
        # 우선 candidates를 정렬
        candidates.sort()
        
        # combinations는 target에 도달하지 못한 조합과 그 합을 저장하는 집합
        combinations = set((((), 0),))
        answer = set()
        
        for num in candidates:
            tmp_combinations = combinations.copy()
            
            for combination, tmp_sum in combinations:
                # 각 숫자가 등장할 떄마다 새로운 조합과 그 합을 만듦
                new_combination = combination + (num, )
                new_sum = tmp_sum + num
                # 새로운 합이 target보다 작을 경우
                # 새로운 조합을 추가한다.
                if new_sum < target:
                    tmp_combinations.add((new_combination, new_sum))
                else:
                    # target과 같을 경우 answer에 추가한다.
                    if new_sum == target:
                        answer.add(new_combination)
                    # 새로운 합이 target보다 크거나 같을 경우, 
                    # num 이후의 숫자는 num보다 크거나 같으므로 더 이상 target과 같아지는 일이 없다.
                    # 따라서 더 이상 볼 필요가 없으므로 집합에서 제거한다.
                    tmp_combinations.remove((combination, tmp_sum))
            combinations = tmp_combinations
        
        return answer

