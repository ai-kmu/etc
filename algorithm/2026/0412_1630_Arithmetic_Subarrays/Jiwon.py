class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        queryLen = len(l)
        ans = [True] * queryLen

        for i in range(queryLen):
            # 검사할 subarray (정렬까지)
            tmp = sorted(nums[l[i]:r[i]+1])

            # 길이 2 이하면 무조건 True임
            if len(tmp) <= 2:
                ans[i] = True
                continue

            # 아닐 경우 등차수열 검사해야 하므로 공차를 anchor로 설정
            anchor = tmp[1] - tmp[0]

            # 돌면서 등차수열 아닌 경우는 False처리하고 다음 subarray 검사
            for j in range(2, len(tmp)):
                if tmp[j] - tmp[j-1] != anchor:
                    ans[i] = False    
                    break
        
        return ans
                
