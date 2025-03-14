class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        total_length = len(arr1) + len(arr2)

        arr1.append(float('inf'))
        arr2.append(float('inf'))

        # 이터레이터로 변환
        arr1, arr2 = iter(arr1), iter(arr2)
        next_val1, next_val2 = next(arr1), next(arr2)
    
        for _ in range((total_length + 1) // 2):
            if next_val1 <= next_val2:
                current_val, next_val1 = next_val1, next(arr1)
            else:
                current_val, next_val2 = next_val2, next(arr2)

        # 홀수 길이면 current_val 반환, 짝수 길이이면 (current_val + 최소값) / 2
        return current_val if total_length % 2 else (current_val + min(next_val1, next_val2)) / 2
