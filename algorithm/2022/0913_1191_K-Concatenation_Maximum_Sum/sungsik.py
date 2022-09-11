class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        N = len(arr)
        
        # 다음 for loop으로 3가지를 구함
        # 1. arr의 maximum sublist sum
        # 2. arr의 왼쪽부터 시작한 maximum sublist sum
        # 3. arr의 오른쪽부터 시작한 maximum sublist sum
        tmp_sum = tmp_left_sum = arr[0]
        max_sum = max_left_sum = max(arr[0], 0)
        tmp_right_sum = arr[-1]
        max_right_sum = max(arr[-1], 0)
        for i in range(1, N):
            tmp_sum = max(arr[i], tmp_sum + arr[i])
            max_sum = max(max_sum, tmp_sum)
        
            tmp_left_sum += arr[i]
            max_left_sum = max(max_left_sum, tmp_left_sum)
        
            tmp_right_sum += arr[N-i-1]
            max_right_sum = max(max_right_sum, tmp_right_sum)
        
        if k == 1:
            return max_sum
        else:
            arr_sum = sum(arr)
            # 다음 3가지 중 maximum을 출력
            # 1. arr의 maximum sublist sum
            # 2. arr을 2개 사용함으로써 얻을 수 있는 max_left_sum + max_right_sum
            # 3. 중간에 있는 모든 arr을 더하고 max_left_sum + max_right_sum 까지 더한 값
            return max(max_sum, max_left_sum + max_right_sum, (k-2) * arr_sum + max_left_sum + max_right_sum) % (10 ** 9 + 7)
