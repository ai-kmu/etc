class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:                                             # 길이가 3 이하이면 불가능
            return False
        nums1 = deque(nums)
        nums2 = deque()
        num_before = nums1.popleft()
        while nums1:                                                  # 연속적인 중복은 제거
            num_now = nums1.popleft()
            if num_before != num_now:
                nums2.append(num_before)
                num_before = num_now
        nums2.append(num_now)
        nums = list(nums2)
        used = []
        for i in range(len(nums)-2):                                   # 1 찾기
            if nums[i] in used:                                        # 앞에서부터 차례로 찾기 때문에 한번 본 숫자에 대해선 뒤에서는 만족할 수 없음
                continue
            number1 = nums[i]
            for j in range(i, len(nums)-1):                            # 3 찾기
                if number1 < nums[j]:                                  # 3은 1보다 커야함
                    number2 = nums[j]
                    for k in range(j, len(nums)):                      # 2 찾기
                        if nums[k] < number2 and number1 < nums[k]:    # 2는 3보단 작고 1보단 커야함
                            return True
            used.append(number1)                                       # 한번 본 1번 자리 숫자는 다음에는 안보기 위해 list에 
        return False
        
        
# test case 3개 통과 못해서 다시 풀어야함
