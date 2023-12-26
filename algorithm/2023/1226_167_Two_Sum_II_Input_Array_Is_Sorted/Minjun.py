"""
target - 현재가 numbers에 있으면 return
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            a = target - n
            if a in numbers:
                # 같으면 이웃하게 위치.
                if a == n:
                    return [i+1, i+2]
                j = numbers.index(a)
                return [i+1, j+1]
