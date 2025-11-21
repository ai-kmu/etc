class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # n이 선언되면, 그 범위 안의 값의 list가 채워짐
        # 1~n으로부터 하나씩 확인하면서 list에 있나 확인, 없는거 answer로
        # nums = list(set(nums))

        [1,2,2,3,3,4,7,8] 
        check = []
        for j in range(len(nums)):
            check.append(0)

        for i in nums:
            check[i - 1] += 1
        print(check)
        answer = []
        for k in range(len(check)):
            if check[k] == 0:
                answer.append(k + 1)

        return answer

