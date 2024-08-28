from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        answer = []
        # Counter를 통해 nums에 있는 모든 숫자들의 갯수를 다 세면 (숫자, 갯수)대로 모두 저장됨
        # 이를 갯수가 작은 순서대로 정렬
        # 앞에서부터 가장 작은 두개가 정답이므로 a[:2]에 있는 value 값을 answer에 추가
        a = sorted(list(Counter(nums).items()), key=lambda x: x[1])
        for k, v in a[:2]:
            answer.append(k)
        return answer
