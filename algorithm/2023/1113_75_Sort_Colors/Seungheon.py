from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 2N
        # 개수를 세서 알맞은 위치에 채워넣기
      
        counter = Counter(nums)
        point = 0
        for i in range(3):
            for j in range(counter[i]):
                nums[point] = i
                point += 1
