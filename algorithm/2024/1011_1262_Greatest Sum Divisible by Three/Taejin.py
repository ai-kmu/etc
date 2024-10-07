class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # nums 정렬
        nums.sort()
        
        # 합, 모듈로 3 계산
        sums = sum(nums)
        remainder = sums % 3
        
        # 모듈로 3 = 0이면 영향 없으므로 1, 2만 리스트로
        modulos = [[i for i in nums if i % 3 == j + 1] for j in range(2)]
        
        # sums (mod 3) = 0이면 그대로 합계 반환
        if remainder == 0:
            return sums

        # 아닌 경우 / sums (mod 3) = 1, 2 인 경우
         # 3의 배수를 만드는 최소 방법
            # remainder = 1인 경우 -> 요소에서 나머지가 1인 것 하나 또는 나머지가 2인 것 두개 제외
            # remainder = 1인 경우 -> 요소에서 나머지가 2인 것 하나 또는 나머지가 1인 것 두개 제외
        else:
            # 최솟값 초기화
            mins = nums[-1]
            
            if modulos[remainder - 1]:
                mins = modulos[remainder - 1][0]
            
            if len(modulos[2 - remainder]) >= 2:
                mins = min(mins, sum(modulos[2 - remainder][:2]))

            return sums - mins
