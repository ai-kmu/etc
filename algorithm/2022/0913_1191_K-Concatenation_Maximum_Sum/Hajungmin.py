class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        cur = 0
        max_num = 0
        loop_one = 0
        
        # 루프를 2번 돌면서 두 가지의 maximum sum을 구한다
        # 첫 번째 루프 안에 maximum sum이 있는 경우와
        # 두 번째 루프 안에 maximum sum이 있는 경우
        for i in range(2):
            for j in arr:
                cur += j
            
                if cur < 0:
                    cur = 0
                
                max_num = max(max_num, cur)
                
            if i == 0: loop_one = max_num
        
        # 만약 k가 1이라면 첫번째 루프에서 maximum sum을 return해준다.
        if k == 1: return loop_one
        
        # 위에서 두 가지의 루프에 대해 maximum sum을 구한 것을 이용해서
        # 0, 루프 1번 돈 것, 루프 2번 돈 것, 루프가 모두 연결되어 있는 경우를 고려해서 max를 구함
        # 모든 루프가 연결되어 있다면 ex) [1,2,1,2,1,2,1,2] -> 두 번의 루프 + arr의 합을 k-2번 한 것
        return int(max(0, loop_one, max_num, max_num + (k - 2) * sum(arr)) % (10**9+7))
