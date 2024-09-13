class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1 = [i for i in word1]
        word2 = [i for i in word2]
        n,m = len(word1), len(word2)
        cnt_n, cnt_m = 0,0
        ans = ''
        while True:
            if cnt_n + cnt_m == n+m:
                break
            elif cnt_n > n-1:
                ans += word2[cnt_m]
                cnt_m += 1
            elif cnt_m > m-1:
                ans += word1[cnt_n]
                cnt_n += 1
            else:
                ans += word1[cnt_n]
                ans += word2[cnt_m]
                cnt_n +=1
                cnt_m +=1
        return ans
