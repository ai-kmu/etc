from collections import defaultdict

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        answer = 1
        # time limit과 memory limit을 해소하기 위한 방법
        # 1. 이전 step에서 만들어진 array들만 저장
        # 2. array의 모든 값을 저장할 필요 없이 최댓값, 최솟값만 저장
        # 3. 겹치는 array들이 많은 경우를 위해 counter 형태로 저장
        arrays = defaultdict(int)
        arrays[(nums[0], nums[0])] = 1
        
        for i, n in enumerate(nums[1:], 1):
            new_arrays = defaultdict(int)
            for (max_val, min_val), count in arrays.items():
                # 최솟값보다 크지만 최솟값과의 차이가 2 이하면 가능
                if n >= min_val and n - min_val <= 2:
                    new_arrays[(max(n, max_val), min_val)] += count
                # 최댓값보다 작지만 최댓값과의 차이가 2 이하면 가능
                elif n <= max_val and max_val - n <= 2:
                    new_arrays[(max_val, min(n, min_val))] += count
            
            new_arrays[(n, n)] += 1
            answer += sum(new_arrays.values())
            arrays = new_arrays
        
        return answer
                        
