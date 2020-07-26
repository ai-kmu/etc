class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)                                  # s_len = string 길이
        if s_len==0:                                    # string 없는 경우 체크
            return 0
        max_len = 1
        for i in range(s_len):                          # 모든 경우의 수 탐색
            temp_list = list()       
            if max_len >= s_len-i:
                break
            for i_s, c in enumerate(s[i:]):             # 같은 문자 나올때까지 탐색
                if c not in temp_list:
                    temp_list.append(c)
                    max_len = max(max_len,len(temp_list))
                    continue
                max_len = max(max_len,len(temp_list))   # max값 갱신
                break
        return max_len
