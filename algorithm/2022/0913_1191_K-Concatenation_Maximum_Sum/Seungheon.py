class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        
        def explore(arr):
            
            for i in range(1, len(arr)):
                # 현재값이 양수일떄
                    # 이전값 + 현재값이 현재값보다 크면 현재값을 이전값 + 현재값 로 수정
                # 현재값이 음수일때
                    # 이전값 +현재값이 양수면 계속 더하고 아니면 0
                if arr[i]>=0:
                    arr[i] = arr[i] if arr[i] > arr[i] + arr[i-1] else arr[i] + arr[i-1]
                else: 
                    arr[i] = arr[i] + arr[i-1] if 0 < arr[i] + arr[i-1] else 0 
   
            return max(arr)
        
        # 앞에서 혹은 뒤에서 부터 더했을때 최대값 구하기
        def max_sum_num(arr):
            sum_num = 0
            max_num = 0
            for n in arr:
                sum_num += n
                max_num = max(sum_num, max_num)            
            return max_num
        
        # k = 1 일때는 일반탐색, k 가 1보다 클때는 max_sum_num 더해줌
        if k == 1:
            return explore(arr*k) % (10**9 + 7)
        else:
            return max(explore(arr*2), sum(arr)*(k-2) + max_sum_num(arr) + max_sum_num(arr[::-1])) % (10**9 + 7)
