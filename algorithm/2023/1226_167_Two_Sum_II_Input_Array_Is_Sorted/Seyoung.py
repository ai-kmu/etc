class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        
        # 목표값에 도달하기 위해 더하기
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        
        # 1부터 시작하는 인덱스로 변환 후 반환
        return [left + 1, right + 1]
