class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        formatting = "0" + str(n) + "b"
        int_list = []

        # nums를 10진수로 변환해서 저장
        for bin_num in nums:
            bin_num = "0b" + bin_num
            int_list.append(int(bin_num, 2))

        # 가능한 범위 내에서 존재하지 않는 수 탐색
        for i in range(n**2+1):
            if i not in int_list:
                # 자릿수 맞춰서 2진수 -> 10진수로 리턴
                return format(i , formatting)
