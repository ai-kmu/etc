class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        longest = 1
        check = [False for i in range(len(nums))]   # 방문했는지 check list
        for i in range(len(nums)):                  # 모든 값 하나씩 방문
            locator = nums[i]                       # 하나 추가하고 시작
            answer = 1
            check[i] = True
            
            while check[locator]==False:            # 방문 안한 것만 통과
                check[locator] = True               # 방문 표시
                locator = nums[locator]             # 다음 방문지
                answer += 1                         # 횟수 기록
                
            if longest < answer:                    # 가장 긴 것 기록
                longest = answer
        return longest
