class Solution:
      def threeSumClosest(self, nums, target):
        """
        이진탐색 방법:
        1. 먼저 숫자들을 오름차순으로 정리한다
        2. 왼쪽에서 시작하는 인덱스 l과 오른쪽에서 시작하는 인덱스 r을 두고 
           만약 현재 인덱스, l번째 인덱스, r번째 인덱스를 더한 값이 target과 같으면 그 값을 리턴
           만약 더한 값과 타겟의 차이가 맨처음 더한 result와 타겟과의 차이보다 작으면 result갱신
           먄약 s가 타겟보다 작으면 더 큰값을 더해줘야하기때문에 왼쪽에서 한칸 이동하고
               s가 타겟보다 크면 더 작은 값을 더해줘야 하기때문에 오른쪽에서 왼쪽으로 이동해야 함
        """
        nums.sort()
        result = sum(nums[:3])
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp == target:
                    return temp
                if abs(temp - target) < abs(result - target):
                    result = temp
                if temp < target:
                    l += 1
                elif temp > target:
                    r -= 1
        return result

        
