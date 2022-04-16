class Solution(object):
    def PredictTheWinner(self, nums): 
        
        # nums의 길이가 짝수일때는 
        # 짝수번째 수의 합과 홀수번쨰 수의 합을 계산하여 첫번Wo player가 할상 승리할 수 있음
        
        # nums의 길이가 홀수일때는 
        # 두 player는 항상 최선의 값 선택
        # player_1이 선택을하고나면 짝수개의 길이가 됨으로
        # player_1 - player_2 의 값이 짝수번째 수의 합과 홀수번쨰 수의 합 의 차보다 작아지면
        # player_1은 무조건 패배하게된다. 
        
        # 홀수번째의 합과 짝수번째의 합 계산
        def half_sum(nums_list):
            even_sum = 0
            for even in range(0, len(nums_list), 2):
                even_sum += nums_list[even] 
            odd_sum = sum(nums_list) - even_sum
            return even_sum - odd_sum
        
        # 끝값중 큰 수 선택
        def bigger_number(nums_list, player):  
            if nums_list[0] > nums_list[-1]:
                point = nums_list[0] 
                nums_list = nums_list[1:]
            else: 
                point = nums_list[-1]
                nums_list = nums_list[:-1]
                
            player += point 
            return nums_list, player             
        
        # player의 score 초기화
        player_1 = 0
        player_2 = 0
        
        # nums의 길이가 짝수일때 player_1이 승리
        if len(nums) % 2 == 0 :
            return True
        
        while nums:
            print(player_1, player_2)
            
            if len(nums) == 1:
                player_1 += nums[0]
                return True if player_1 >= player_2 else False
            
            # player_1의 선택
            nums, player_1 = bigger_number(nums, player_1)
            
            # player_1의 패배조건 확인
            if player_1 - player_2 < abs(half_sum(nums)): 
                return False
            
            # player_2의 선택
            nums, player_2 = bigger_number(nums, player_2)
