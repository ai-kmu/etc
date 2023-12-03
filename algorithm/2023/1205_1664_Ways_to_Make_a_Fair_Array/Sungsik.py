class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # 미리 짝수합과 홀수합을 구해놓는다
        odd_sum = sum(nums[1::2])
        even_sum = sum(nums[2::2])
        
        answer = int(odd_sum == even_sum)
        
        prev_num = nums[0]
        
        for i, num in enumerate(nums[1:], 1):
            # 현재 숫자의 위치에 따라
            # 짝수합이나 홀수합에 num을 빼고 prev_num을 넣을지 결정
            if i % 2 == 0:
                even_sum += prev_num - num
            else:
                odd_sum += prev_num - num

            if odd_sum == even_sum:
                answer += 1
            prev_num = num
        
        return answer
