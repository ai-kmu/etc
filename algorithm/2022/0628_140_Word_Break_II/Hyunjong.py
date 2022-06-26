# 실패
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        num_s = len(s)
        set_word = set(wordDict)
        for i in range(num_s):
            for j in range(i + 1, num_s + 1):
                if s[i : j] in set_word:
                    print(s[i : j])
