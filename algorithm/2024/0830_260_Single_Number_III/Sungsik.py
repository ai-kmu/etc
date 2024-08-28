class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        appear = set()
        for num in nums:
            # 등장 안했을 경우 추가
            if num not in appear:
                appear.add(num)
            # 했을 경우 지움
            else:
                appear.remove(num)
        return list(appear)
