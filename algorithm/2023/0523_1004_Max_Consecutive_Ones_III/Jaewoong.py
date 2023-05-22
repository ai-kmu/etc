class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        windowStart = 0
        windowZeros = 0
        windowOnes = 0
        maxOnes = 0
        # nums의 길이만큼 수행 예정
        for windowEnd in range(len(nums)):
            # 0을 찾으면
            if nums[windowEnd] == 0:
                # k만큼 수행이 끝나지 않은 경우
                if windowZeros < k:
                    # 1 더하고
                    windowZeros += 1
                # 아니면 다 뒤집었다는 뜻이니까
                else:
                    # 1이 아닌수가 나올 때까지 반복
                    while(nums[windowStart] == 1):
                        # 한칸씩 이동
                        windowStart += 1
                        windowOnes -= 1
                    windowStart += 1
            # 0을 못찾고 1이 나온 경우
            elif nums[windowEnd] == 1:
                # 길이 = windowone 1증가
                windowOnes += 1 
                # 매 회 최신화
                maxOnes = max(maxOnes, windowOnes) 
        return maxOnes + windowZeros
