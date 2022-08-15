# 아래와 같은 알고리즘을 거치면 된다.

# 1. 정답 리스트에 우선 nums의 첫번째 값을 집어 넣는다.
# 2. 그 후 nums를 탐색하며 만일 nums에 정답 리스트의 마지막 값보다 작은 값이 있으면 정답 리스트 중 nums보다 작은 값을 찾아 그 수 앞에 집어 넣어준다(덮어쓰기).
# 3. 2번을 계속 반복한다.

# 위 알고리즘을 이용하면 완벽한 LIS 리스트가 만들어 지지는 않지만 적어도 길이는 확실히 알게해준다.
# 위 알고리즘은 만약 i번째 부터 LIS를 쌓으면 어떻게 될지를 탐색하는 알고리즘이다.



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def bs(left, right, target): # binary search로 target보다 큰 수중 가장 작은 수를 탐색하낟.
            while left < right:
                mid = int((left+right) / 2)
                if ans[mid] < target:
                    left = mid + 1
                else:
                    right = mid
        
            return right
            
        ans = [nums[0]] # 우선 ans에 nums의 첫번째 값을 넣어놓고 시작한다.
        for n in nums[1:]:
            if ans[-1] < n: # ans의 마지막 값보다 n이 크면 그냥 append한다.
                ans.append(n)
            else: # ans의 마지막 값보다 n이 작으면 알맞은 위치를 찾아 ans 배열에 덮어쓰기 해준다.
                ans[bs(0,len(ans), n)] = n
        
        return len(ans)            
