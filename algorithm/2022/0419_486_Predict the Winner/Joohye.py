'''
dp 실패 -> recursion java 풀이 참조
'''

class Solution:
    def winner(self, nums, start, end, turn):  
        # 마지막 선택일 경우
        if (start == end):  
            return turn * nums[start]  # nums[end]도 가능, 마지막 남은 수를 return
        
        # player 1 인 경우 turn = 1(max값 구해야함), player 2 인 경우 turn = -1(min값 구해야함)
        return turn * max(nums[start] + turn * self.winner(nums, start + 1, end, -turn),      
                          nums[end] + turn * self.winner(nums, start, end - 1, -turn))
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # player 1 이 이기는 경우 = player 1(양수 값)+ player 2(음수 값)이 비기거나 양수인 경우
        return self.winner(nums, 0, len(nums) - 1, 1) >= 0;  
    
