class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # 중복 제거를 위해 set으로 answer를 초기화
        answer = set()
        def back(num_list, res, idx):
            # 인덱스를 기준으로 candidates를 순회
            if idx == len(candidates):
                return
            num = candidates[idx]
            new_res = res - num
            # 남은 값이 target과 동일해지면 answer에 추가
            # 정답은 숫자들의 순서를 고려하지 않으므로 정렬
            if new_res == 0:
                answer.add(tuple(sorted(num_list + [num])))
                return
            # 남은 값이 0보다 작으면 더 순회하지 않음
            elif new_res < 0:
                return
            else:
                # candidates에서 숫자를 뽑는 건 중복을 허용하므로 두 가지 경우를 고려
                # 1. 현재 인덱스를 다시 진행하기
                num_list.append(num)
                back(num_list, new_res, idx)
                # 2. 돌아와서 다음 인덱스로 진행하기
                num_list.pop()
                back(num_list, res, idx + 1)
        
        back([], target, 0)
        return list(answer)
