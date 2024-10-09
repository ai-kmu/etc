class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 우선 최대 합을 구하는 것이기 때문에 전체 합으로부터 3의 배수를 만들기 위한 가장 작은 값들을 뺌
        answer = sum(nums)
        nums.sort()
        # 정렬한 nums 중에 나머지가 1이 되는 것들과 2가 되는 것들을 구해줌
        nam_1, nam_2 = [], []
        for i in nums:
            if i % 3 == 1:
                nam_1.append(i)
            elif i % 3 == 2:
                nam_2.append(i)

        # 만약 합이 이미 3의 배수라면 바로 return
        # 합의 나머지가 1인 경우 나머지가 1인 숫자 중 하나를 빼주거나 2인 숫자 2개를 빼준 옵션 중 더 큰 옵션을 리턴
        # 합의 나머지가 2인 경우 나머지가 1인 숫자 두개를 빼주거나 2인 숫자 하나를 빼준 옵션 중 더 큰 옵션을 리턴
        # 옵션 중 불가능한 경우(필요 개수를 충족하지 못했을 경우)에는 해당 옵션을 0으로 만들어줌
        if answer % 3 == 0:
            return answer
        elif answer % 3 == 1:
            option_1 = answer - nam_1[0] if nam_1 else 0
            option_2 = answer - sum(nam_2[:2]) if len(nam_2) > 1 else 0
        else:
            option_1 = answer - sum(nam_1[:2]) if len(nam_1) > 1 else 0
            option_2 = answer - nam_2[0] if nam_2 else 0
        return max(option_1, option_2)
        
