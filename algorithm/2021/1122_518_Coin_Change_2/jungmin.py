class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
      
        # Dynamic Programming
        w = [0] * (amount+1) # amount만큼 만들 수 있는 경우의 수를 저장하는 리스트 w 생성
        w[0] = 1 # 0원을 만들 수 있는 경우의 수는 아무것도 없는 오직 하나이므로 0 인덱스의 값은 1로 저장
        

        for c in coins:
            for i in range(1, amount+1):
                if c <= i: # coins 안에 있는 코인 하나 c는 자기 자신 만큼의 amount보다 작은 amount를 생성할 수 없음.
                    # i원을 c원으로 만들 수 있는 경우의 수는 이전 코인 c까지 i원을 만들 수 있는 경우 수에다가 i에서 현재 코인 c를 뺀 값을 만드는 경우의 수를 더한다.
                    # 이 때 현재 amount에서 현재 코인 c를 뺀 값을 만드는 경우의 수는 이전에 계산했던 값을 다시 불러오도록 한다.
                    w[i] = w[i] + w[i-c] 
                    
        return w[-1] # 구하고자 하는 amount의 경우의 수를 출력한다.
