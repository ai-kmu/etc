class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        dp = [[ 0 for _ in sequence ] for _ in word]

        for word_i, word_char in enumerate(word):
            for seq_i, seq_char in enumerate(sequence):
                if word_i == 0 :
                    dp[word_i][seq_i] = 1 if word_char == seq_char else 0
                else:
                    if seq_i >= word_i and dp[word_i-1][seq_i-1] == 1 and word_char == seq_char:
                        dp[word_i][seq_i] = 1 
                        
        for i in dp:
            print(i)

        answer_dp = [ 0 for _ in dp[-1]]
        for i, c in enumerate(dp[-1]):
            if i >= len(word) - 1:
                if dp[-1][i] == 1:
                    answer_dp[i] = answer_dp[i-len(word)] + 1

        # print(answer_dp)
        return max(answer_dp)
