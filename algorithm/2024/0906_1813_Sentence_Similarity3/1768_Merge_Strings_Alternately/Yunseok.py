class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_len = len(word1)
        w2_len = len(word2)

        if w1_len > w2_len:
            smallest_len = w2_len
            max_len = w1_len
            max_str = word1
        else:
            smallest_len = w1_len
            max_len = w2_len
            max_str = word2

        output_str = ""
        for idx in range(smallest_len):
            output_str += word1[idx]
            output_str += word2[idx]
        
        output_str += max_str[smallest_len: max_len]
        return output_str
