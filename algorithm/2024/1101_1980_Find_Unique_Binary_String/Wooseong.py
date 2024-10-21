class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        digit = len(nums[0])  # 자릿수 확인
        appear = set(nums)  # 빠른 탐색을 위해 set으로 변경
        
        # 10진수로 표현된 nums에 담길 수 있는 것들 중에 탐색
        for decimal in range(2 ** digit):
            # `bin`으로 2진수 변환 / `[2:]`로 "0b" 제거 / `rjust`로 0 채우기
            binary = str(bin(decimal))[2:].rjust(digit, '0')
            # 없으면 그거 바로 return
            if binary not in appear:
                return binary
