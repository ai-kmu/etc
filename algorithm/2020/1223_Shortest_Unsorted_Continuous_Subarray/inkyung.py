class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        idx_list = list()                       # 바꿔주야 하는 숫자들의 인덱스를 저장
        sort_nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != sort_nums[i]:
                idx_list.append(i)
        if not idx_list:                        # 바꿔주지 않아도 되면 0 리턴
            return 0
        return idx_list[-1] - idx_list[0] + 1   # 제일 마지막 인덱스와 제일 처음의 인덱스의 차이를 구하면 됨
