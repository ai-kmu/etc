class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        # recurrent를 위한 함수 정의
        def supporter(nums):
            n = len(nums)
            # 길이가 1일 때 종료
            if n == 1:
                return nums
            # 길이 절반으로 줄인 newNums 할당
            a, b = divmod(n, 2)
            new_n = a + b
            new_nums = [None for _ in range(new_n)]
            # 짝수 처리
            for i in range(0, new_n, 2):
                new_nums[i] = min(nums[2 * i], nums[2 * i + 1])
            # 홀수 처리
            for i in range(1, new_n, 2):
                new_nums[i] = max(nums[2 * i], nums[2 * i + 1])
            # recurrent 처리
            return supporter(new_nums)

        # 다 끝나고 나온 1짜리 리스트의 item 반환
        return supporter(nums)[0]
