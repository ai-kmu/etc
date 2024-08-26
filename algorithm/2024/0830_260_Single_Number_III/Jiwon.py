class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        
        # Counter를 통해 요소 개수 세어줌
        counter = Counter(nums)
        
        # 두 번 등장한 요소는 삭제
        for i in list(counter):
            if counter[i] == 2:
                del counter[i]
 
        return list(counter)
