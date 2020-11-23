class Solution(object):
    def arrayNesting(self, nums):
        max_ = 0
        for ind in range(len(nums)):  # 첫 단추 어느 인덱스에서 낄지 결정
            count = 0
            curr = ind
            while nums[curr]>=0:  # 재방문한 자리가 생길때까지 반복
                ind_value = nums[curr] # 반환된 숫자 저장해서 다음 인덱스
                nums[curr] = -1 # 한번 방문한 자리는 -1로 대체
                curr = ind_value
                count += 1
            max_= max(max_, count)  # 가장 큰 수 반환
            
        return max_
