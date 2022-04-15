class Solution:
    def solution(self, left_index, right_index, turn):
        player = turn % 2 # 0이면 player1, 1이면 player2
        
        # 카드 두장이 남은 경우
        if turn == len(self.nums) - 2:
            # 현 상태의 player가 더 높은 점수의 카드를 가질 수 있다.
            # 남은 카드 중 어떤 카드가 더 높은 점수일지 저장해주자
            high_score_card = max(self.nums[left_index], self.nums[right_index])
            low_score_card = min(self.nums[left_index], self.nums[right_index])
            # 한번에 두개의 값을 리턴한다.
            # 왼쪽은 player1의 점수이다.
            # 오른쪽은 player2의 점수이다.
            if player == 0:
                return high_score_card, low_score_card
            else:
                return low_score_card, high_score_card
        
        # 카드가 세 장 이상 남은 경우
        # dfs를 통해 솔루션을 찾는다.
        # lc_score0과, lc_score1은 현 상태에서 플레이어가 왼쪽을 뽑았을 경우 리턴되는 값이다.
        # rc_score0과, rc_score1은 현 상태에서 플레이어가 오른쪽을 뽑았을 때 리턴되는 값이다.
        lc_score0, lc_score1 = self.solution(left_index + 1, right_index, turn + 1)
        rc_score0, rc_score1 = self.solution(left_index, right_index - 1, turn + 1)
        
        # 현재 남아 있는 카드 중 자신이 최대한의 점수를 얻을 수 있게끔 해야한다
        # 만약 현재 카드를 뽑는 플레이어가 1번 플레이어일 경우
        if player == 0:
            # 왼쪽을 뽑았을 경우 점수는 다음과 같이 정의된다.
            # 제일 왼쪽에 있는 카드의 점수 + 왼쪽을 뽑았을 경우 얻을 점수값 
            lc_score0 += self.nums[left_index]
            # 오른쪽을 뽑았을 경우도 점수를 다음과 같이 정의할 수 있다.
            # 제일 오른쪽에 있는 카드의 점수 + 오른쪽을 뽑았을 때 얻을 점수값
            rc_score0 += self.nums[right_index]
            # 플레이어는 최대한의 점수를 얻을려고 하기 때문에
            # 자신에게 유리한 경우를 골라 이를 리턴한다.
            if lc_score0 >= rc_score0:
                return lc_score0, lc_score1
            else:
                return rc_score0, rc_score1
        # 2번 플레이어도 자신에게 유리한 상황을 골라 리턴하려고 할 것이다.
        else:
            lc_score1 += self.nums[left_index]
            rc_score1 += self.nums[right_index]
            if lc_score1 >= rc_score1:
                return lc_score0, lc_score1
            else:
                return rc_score0, rc_score1
        
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.nums = nums
        # 만약 카드가 한장이라면
        # 플레이어 1이 무조건 이김
        if len(nums) == 1:
            return True
        
        # score0과 socre1에는 두 플레이어가 치열하게 싸운 결과가 리턴된다
        score0, score1 = self.solution(0, len(nums) - 1, 0)
        # player0의 점수가 더 높다면 승리하게 된다.
        if score0 >= score1:
            return True
