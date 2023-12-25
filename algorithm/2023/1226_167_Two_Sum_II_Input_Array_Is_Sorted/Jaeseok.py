from bisect import bisect_left

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 제일 왼쪽과 제일 오른쪽에서부터 탐색
        l, r = 0, len(numbers) - 1
        while l <= r:
            # res : 가장 오른쪽의 숫자에서 뺀 나머지
            res = target - numbers[r]
            # bisect를 활용하여 res와 가장 가까운 수를 찾음
            l = bisect_left(numbers, res)
            # 만약 그 수가 res와 동일하지 않다면 r을 1 줄여서 다시 탐색
            if numbers[l] != res:
                r -= 1
            # 만약 그 수가 res와 동일하다면 정답은 unique하므로 return
            else:
                return [l + 1, r + 1]
        
