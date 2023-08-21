class Solution(object):
    def getHappyString(self, n, k):

        char_list = ['a', 'b', 'c']

        # 재귀적으로 탐색
        def make_list(prv_chr='@', ch_list=[], tmp_list=[]):
            # 길이가 n 이되면 그만 탑색하고 값을 tmp_list에 저장
            if len(ch_list) == n:
                tmp_list.append(''.join(ch_list))
                return tmp_list
            
            # 같은 char이 아닐때만 탐색
            for i, ch in enumerate(char_list):
                if prv_chr == ch:
                    continue
                tmp_list = make_list(ch, ch_list + [ch], tmp_list)

            return tmp_list

        tmp_list = make_list()
        tmp_list.sort()
        
        # 범위 밖이면 ""를 return
        try:
            return tmp_list[k-1]
        except:
            return ""
