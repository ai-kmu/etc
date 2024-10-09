# 나머지는 0, 1, 2의 경우만 존재
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        one_list, two_list = [], []
        total = sum(nums)

        for num in nums:
            # 나머지가 1인 경우
            if num % 3 == 1:  
                one_list.append(num)
            # 나머지가 2인 경우 
            elif num % 3 == 2:  
                two_list.append(num)
        
        one_list.sort()
        two_list.sort()

        if total % 3 == 1:
            # 나머지 1인 숫자 중 가장 작은 값을 빼서 3의 배수로 
            if one_list and (len(two_list) < 2 or sum(two_list[:2]) > one_list[0]):
                total = total - one_list[0]
            # 나머지 2인 숫자 중 작은 두 개의 값을 빼서 3의 배수로
            elif len(two_list) > 1: 
                total = total - two_list[0] - two_list[1]  
        elif total % 3 == 2:
            # 나머지 2인 숫자 중 가장 작은 값을 빼서 3의 배수로
            if two_list and (len(one_list) < 2 or sum(one_list[:2]) > two_list[0]):
                total = total - two_list[0]  
            # 나머지 1인 숫자 중 작은 두 개의 값을 빼서 3의 배수로
            elif len(one_list) > 1: 
                total = total - one_list[0] - one_list[1]  

        return total
