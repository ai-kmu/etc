class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        # nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])는 아래와 같이 변형할 수 있다.
        # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
        
        d = defaultdict(int) # 딕셔너리 d 생성
        # 딕셔너리 d에 원래의 수에서 역순의 수를 뺀 값을 key로 하여 1씩 더함
        for i in nums:
            rev_value = int(str(i)[::-1])
            d[i-rev_value] += 1
        
        ans = 0
        # 딕셔너리의 value는 각 nums[i] - rev(nums[i])의 갯수이며
        # 조합 combination 식 (nC2)를 이용하여 계산가능
        for v in d.values():
            ans += (v*(v-1)//2)
            
        return ans % (10**9+7)
