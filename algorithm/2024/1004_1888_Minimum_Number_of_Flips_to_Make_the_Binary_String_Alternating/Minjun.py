# 솔루션봤음

import sys

class Solution(object):
    def minFlips(self, s):
        n = len(s)  # we save this length as it is length of window
        s += s  # we add this string because we can have any possibility like s[0]->s[n-1] or s[2]->s[n+1]meaning is that any continous variation with n length ...
        ans = sys.maxsize  # assigning the answer max possible value as want our answer to be minimum so while comparing min answer will be given
        ans1, ans2 = 0, 0  # two answer variables telling amount of changes we require to make it alternative
        s1 = ""  # dummy string like 10010101
        s2 = ""  # dummy string like 01010101

        for i in range(len(s)):
            if i % 2 == 0:
                s1 += "1"
                s2 += "0"
            else:
                s1 += "0"
                s2 += "1"

        for i in range(len(s)):
            if s[i] != s1[i]:  # if they dont match we want a change so ++1
                ans1 += 1
            if s[i] != s2[i]:
                ans2 += 1

            if i >= n:
                # now we have gone ahead so removing the initial element
                # but wait if that element needed a change we added ++ earlier but now he is not our part
                # so to nullify its ++ we did a -- in string
                if s[i - n] != s1[i - n]:
                    ans1 -= 1
                if s[i - n] != s2[i - n]:
                    ans2 -= 1

            # when i reaches n-1 we have n length so we check answer first time
            # and after that we always keep seeing if we get a less answer value and after the loop we get
            if i >= n - 1:
                ans = min([ans, ans1, ans2])

        return ans
