from bisect import bisect_left


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 앞에서부터 순회하면서 target-num을 binary search로 찾음
        # O(nlogn)
        for i, n in enumerate(numbers):
            tmp_target = target - n
            tmp_numbers = numbers[:i] + numbers[i+1:]
            
            tmp_idx = bisect_left(tmp_numbers, tmp_target)
            try:
                if tmp_target == tmp_numbers[tmp_idx]:
                    # tmp_idx는 i를 빼고 계산한 값이므로
                    # 2를 더함
                    return (i+1, tmp_idx+2)
            except IndexError:
                continue
