class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        tmp_list = []
        answer = ''
        for i in s:
            if i != '':
                tmp_list.append(i)

        for i in tmp_list[::-1]:
            answer += i
            answer += ' '
            

        return answer[:-1]
