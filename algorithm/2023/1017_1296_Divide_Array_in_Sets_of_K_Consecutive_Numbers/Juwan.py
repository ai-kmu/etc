class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:

        N = len(nums) # nums의 길이

        if N % k != 0: # 만약 길이부터 나누어지지 않으면 false 리턴
            return False

        nums.sort() # 정렬 리스트 활용

        while nums: # nums가 남아있는 동안
            cur = nums[0]
            cnt = k

            while cnt: # k번을 돌면서
                if cur not in nums: # 만약 순차적으로 cur을 증가시켰을 때 nums에 없으면
                    return False    # 선형적 증가가 아니므로 false 리턴
                nums.remove(cur) # 사용한 cur을 nums에서 제거
                cnt -= 1 # 제거했으면 cnt도 줄여야함
                cur += 1 # cur의 순차적 증가

        return True
