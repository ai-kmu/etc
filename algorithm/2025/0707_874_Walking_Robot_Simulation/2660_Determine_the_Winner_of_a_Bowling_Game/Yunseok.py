class Solution:
    def count_score(self, player1):
        p1_score = 0
        for idx, score in enumerate(player1):
            # print("current_idx: ", idx)
            current_score = score
            for prev_idx in [idx - 1, idx - 2]:
                if prev_idx >= 0 and player1[prev_idx] == 10:
                    current_score *= 2
                    break

            p1_score += current_score
        return p1_score

    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        score_1 = self.count_score(player1)
        score_2 = self.count_score(player2)

        print(score_1)
        print(score_2)

        if score_1 > score_2:
            return 1
        elif score_1 < score_2:
            return 2
        else:
            return 0
        
