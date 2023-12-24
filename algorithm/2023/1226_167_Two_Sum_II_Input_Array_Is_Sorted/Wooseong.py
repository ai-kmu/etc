# two pointer
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 왼쪽, 오른쪽 끝에 pointer 지정
        low = 0
        high = len(numbers) - 1
        
        # 합이 target과 같을 때까지 반복
        sum_ = numbers[low] + numbers[high]
        while sum_ != target:
            # 합이 더 크다면 큰 값을 당겨옴
            if sum_ > target:
                high -= 1
            # 합이 더 작다면 작은 값을 당겨옴
            elif sum_ < target:
                low += 1
            # 합 갱신
            sum_ = numbers[low] + numbers[high]
        
        # 출력 index는 python과 달리 1부터하라고 했으므로 +1 해서 출력
        return [low + 1, high + 1]
