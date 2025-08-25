class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1  # 첫 번째 값은 항상 고유함
        for i in range(1, len(nums)):
            # i번째에 새로운 게 나온다면
            # ps. k-1인 건 인덱스가 0부터 시작하기 때문
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]  # 다음 위치 (k-1 + 1)에 갖고오고
                k += 1  # k 증가
        return k
