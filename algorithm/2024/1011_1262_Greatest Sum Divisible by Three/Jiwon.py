class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # 전부 더 해서 3으로 나누어지면 그대로 반환
        sum_of_num = sum(nums)
        if sum_of_num % 3 == 0:
            return sum_of_num
        
        # 그게 아닐 경우 전체 리스트 순회하며 나머지를 남기는 원소를 체크
        mod_one = list()
        mod_two = list()

        for num in nums:
            if num % 3 == 1:
                mod_one.append(num)
            elif num % 3 == 2:
                mod_two.append(num)

        mod_one.sort()
        mod_two.sort()
        ans = 0

        # 나머지 1일 때 두 가지 옵션이 가능함
        # 1. 나머지 1인 값 중 가장 작은 값 빼기
        # 2. 나머지 2인 값 중 작은 순으로 두 개 빼기
        # 둘 중 더 큰 값을 반환, 나머지 2일 때도 마찬가지
        if sum_of_num % 3 == 1:
            if mod_one:
                ans = sum_of_num - mod_one[0]
            if len(mod_two) >= 2:
                tmp = sum_of_num - mod_two[0]- mod_two[1]
                return max(ans, tmp)
        else:
            if mod_two:
                ans = sum_of_num - mod_two[0]
            if len(mod_one) >= 2:
                tmp = sum_of_num - mod_one[0]- mod_one[1]
                return max(ans, tmp)
        return ans
