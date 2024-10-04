"""
:type s: str
:type t: str
:rtype: bool
"""
class Solution(object):
    def isSubsequence(self, s, t):

        if s == '' and t == '':
            return True
        if s =='' and t != '':
            return True

        for i in range(len(t)):
            if s != '':
                if s[0] == t[i]:
                    if len(s) != 1:
                        s = s[1:]
                    else:
                        return True
                else:
                    continue
            else:
                return True
        return False
