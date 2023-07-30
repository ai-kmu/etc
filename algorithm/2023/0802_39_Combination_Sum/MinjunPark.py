class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []

        self.func(target, candidates, [])

        return self.answer


    # 재귀 방식으로 접근
    # target: 0이 될 때 까지 candidates에서 선택된 수를 뺌
    # candidates: target에서 뺄 수 있는 값
    # arr: 지금까지 target에서 뺀 값을 보관하는 배열
    def func(self, target, candidates, arr):
        if target == 0:  # target이 0이면 적합한 combination sum
            self.answer.append(arr)  # 멤버 변수 answer에 append
            return

        elif target < 0:  # target이 음수면 불가능한 case
            return

        for i, v in enumerate(candidates):
            # target == target - v
            # candidates = candidates[i:] (중복 제거를 위해 선택한 수 보다 작은 값 삭제)
            # arr = arr[:] + [v] (선택한 수를 arr에 추가)
            # 위의 조건이 주어진 부분 문제로 해석 가능
            self.func(target - v, candidates[i:], arr[:] + [v])
        
        return
