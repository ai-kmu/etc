class Solution:
    def countNicePairs(self, nums):
        # 요소들간의 수와 수의reverse값의 차가 같으면 nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) 조건을 만족하게된다
        # 따라서 nums에서 수를 하나씩가져와 비교하며 값이 같은 개수만큼 정답값에 추가해준다 
        
        # 기록 할 수 있는 dictionaty 생성
        keyMap = defaultdict(int)
        
        answer = 0
        
        # 값을 하나씩 가져온다
        for num in nums:
            # 수와 수의 차를 확인한다
            key = num - int(str(num)[::-1])
            # 수의 값으로 dictionary의 key값을 가지는 항복이 있으면 value값(차 가 같은 요소들의 개수)를 answer에 추가한다
            answer += keyMap[key]
            # 차가 같은 요소값 이 하나가 늘었으니 value값에 1 더한다
            keyMap[key] += 1

        return answer % (10**9 + 7)
