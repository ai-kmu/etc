class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        # two pointer로 풀이
        while l < r:
            num_sum = numbers[l] + numbers[r]
            # 두 원소의 합이 target과 같다면 해당하는 인덱스를 리턴          
            if num_sum == target:
                return [l+1, r+1]
            elif num_sum > target:
                r -= 1
            else:
                l += 1
                
        return [-1, -1]
