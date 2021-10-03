class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result와 overlap을 초기화 시켜준다.
        result = set()
        overlap1 = set()
        overlap2 = {}
        # enumerate를 통해 nums를 돌며 overlap1에 num1이 없는 숫자라면num1을 추가한다.
        for i, num1 in enumerate(nums):
            #num1이 overlap1에 있다면 중복되는 숫자이기 때문에 nums의 다음 숫자로 넘어간다
            if num1 not in overlap1:
                overlap1.add(num1)
                #nums를 i번째 다음부터 돌며 -num1-num2를 num3로 지정한다.
                for j, num2 in enumerate(nums[i+1:]):
                    num3 = -num1 - num2
                    #overlap2에는 num1,num2를 dictionary형태로 저장해놨다가 num3와 비교하여 정렬된 튜플의 형태로 result에 저장한다.
                    if (num3 in overlap2) and (overlap2[num3] == num1):
                        result.add(tuple(sorted((num1, num2, num3))))
                    overlap2[num2] = num1
        return result
