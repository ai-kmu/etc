class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 색깔에 따른 숫자 저장
        nums_dict = dict()
        nums_dict["red"] = []
        nums_dict["white"] = []
        nums_dict["blue"] = []
        for n in nums:
            if n == 0:
                nums_dict["red"].append(n)
            elif n == 1:
                nums_dict["white"].append(n)
            else:
                nums_dict["blue"].append(n)

        # 딕셔너리에서 저장한 대로 'red','white','blue' 순으로 key을 갖고와서 nums에 있는 숫자 위치 조정
        # 인덱스는 j=0부터 시작해서 nums[j]에 수정할 때마다 j는 1씩 증가
        j = 0
        for d in nums_dict:  # d는 컬러 키 스트링
            for n in nums_dict[d]:  # n은 컬러 안 값들
                nums[j] = n
                j += 1
