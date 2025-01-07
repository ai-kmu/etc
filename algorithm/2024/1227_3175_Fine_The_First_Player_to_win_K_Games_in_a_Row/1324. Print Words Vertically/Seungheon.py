class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s_list = list(s.split(' '))
        
        answer = []
        max_s = 0
        for tmp_s in s_list:
            max_s = max(max_s, len(tmp_s))
        for _ in range(max_s):
            answer.append("")

        for i in range(max_s):
            for s_tmp in s_list:
                if i < len(s_tmp):
                    answer[i] += s_tmp[i]
                else:
                    answer[i] += " "
        new_answer = []
        for i in answer:
            new_answer.append(i.rstrip())
        return new_answer
        
