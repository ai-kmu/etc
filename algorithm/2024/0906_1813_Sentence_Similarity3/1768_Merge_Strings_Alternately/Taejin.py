class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        sub_len = min(len(word1), len(word2))
        ret = [0] * sub_len * 2
        ret[::2] = word1[:sub_len]
        ret[1::2] = word2[:sub_len]
        ret += word1[sub_len:] 
        ret += word2[sub_len:] 

        return "".join(ret)
