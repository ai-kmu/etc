class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        
        for i in range(len(l)):
            # subarray 추출
            subarray = sorted(nums[l[i]:r[i]+1])

            # 판별
            is_arithmetic = True
            diff = subarray[1] - subarray[0]

            for j in range(2, len(subarray)):
                if subarray[j] - subarray[j-1] != diff: # 차이 확잉ㄴ
                    is_arithmetic = False
                    break

            answer.append(is_arithmetic)
        return answer
