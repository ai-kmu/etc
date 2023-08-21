class Solution(object):
    def getHappyString(self, n, k):

        char_list = ['a', 'b', 'c']

        def make_list(prv_chr='@', ch_list=[], tmp_list=[]):
            if len(ch_list) == n:
                tmp_list.append(''.join(ch_list))
                return tmp_list
                
            for i, ch in enumerate(char_list):
                if prv_chr == ch:
                    continue
                tmp_list = make_list(ch, ch_list + [ch], tmp_list)

            return tmp_list

        tmp_list = make_list()
        tmp_list.sort()

        try:
            return tmp_list[k-1]
        except:
            return ""
